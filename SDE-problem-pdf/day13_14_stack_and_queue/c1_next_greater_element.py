"""
--problem--
-----------
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]),
return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
--example--
-----------
Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

--link--
--------
https://leetcode.com/problems/next-greater-element-ii/

complexity
-----------
MEDIUM

"""
# considering this as a no limit stack.
class Stack:
    def __init__(self) -> None:
        self.arr = []
    
    
    def is_empty(self):
        if len(self.arr) == 0:
            return True
        return False

    def peek(self):
        return self.arr[-1]
    
    def size(self):
        return len(self.arr)
    
    def push(self, val):
        self.arr.append(val)
        

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        popped_ele = self.arr.pop()
        return popped_ele

    def print_stack(self):
        print("="*10)
        for i in range(len(self.arr)-1, -1, -1):
            print(self.arr[i])
        print("="*10)


class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n
        s = Stack()

        # iterate from the last index.
        for i in range((2 * n - 1), -1, -1):
            while not s.is_empty() and s.peek() <= nums[i % n]:# since it is circular array index is % n
                s.pop()
        
            # only adding ans from n index is enough:
            if i < n :
                if not s.is_empty():
                    ans[i] = s.peek()
                else:
                    ans[i] = -1
                
            s.push(nums[i % n])# since it is circular array index is % n

        return ans

a = Solution().nextGreaterElements([1,2,3,4,3])
print(a)


# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""