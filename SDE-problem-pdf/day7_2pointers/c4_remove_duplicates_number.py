"""
--problem--
-----------
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

--example--
-----------
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

--link--
--------
https://leetcode.com/problems/remove-duplicates-from-sorted-array/


complexity
-----------
EASY

"""



class Solution:
    def removeDuplicates(self, nums):
        """
        step 1: iterative over the list using b pointer.
        step 2: a pointer needs to track the 
        """
        a = 0
        for b in range(1,len(nums)): # acts us a b pointer
            print("a,b",a,b)
            if nums[a] != nums[b]:
                a += 1
                nums[a] = nums[b]
                print("looks not same swap")
            print(nums)
        print(nums)
        return a + 1
        

a = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(a)
# time and space complexity
# -------------------------
# time --> O(N)
# space -> O(1)

# output
"""
a,b 0 1
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
a,b 0 2
looks not same swap
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
a,b 1 3
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
a,b 1 4
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
a,b 1 5
looks not same swap
[0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
a,b 2 6
[0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
a,b 2 7
looks not same swap
[0, 1, 2, 3, 1, 2, 2, 3, 3, 4]
a,b 3 8
[0, 1, 2, 3, 1, 2, 2, 3, 3, 4]
a,b 3 9
looks not same swap
[0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
[0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
5
"""