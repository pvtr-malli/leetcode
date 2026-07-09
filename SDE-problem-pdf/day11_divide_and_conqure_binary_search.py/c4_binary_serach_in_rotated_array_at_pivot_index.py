"""
--problem--
-----------
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

--example--
-----------
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

--link--
--------
https://leetcode.com/problems/search-in-rotated-sorted-array/


complexity
-----------
MEDIUM

"""


class Solution:
    def search(self, nums, target):

        # edge case.
        if len(nums) == 1:
            return (0 if nums[0] == target else -1)


        low = 0; high =len(nums)-1
        print("array", nums)
        while high >= low:
            mid = (high+low) // 2

            if nums[mid] == target: return mid
            print("mid", mid)
            # if left part targted. (low - mid)
            if nums[low] <= nums[mid]:
                # target lies in left part:
                if nums[low] <= target and target <= nums[mid]:
                    # go to left part.
                    print(" left sorted and target lies here")
                    high = mid - 1
                else:
                    # go to right part.
                    print(" left sorted and target lies in opposite right side")
                    low = mid + 1

             # if right part targted. (mid - right)
            else:
                # target lies in right part:
                if nums[mid] <= target and target <= nums[high]:
                    # go to right part.
                    print(" right sorted and target lies here")
                    low = mid + 1
                else:
                    # go to left part.
                    print(" right sorted and target lies in opposite left side")
                    high = mid - 1
            print("low, high", low,high)
        return -1 # when target not present in array.


a= Solution().search( [4,5,6,7,0,1,2], 3)
print(a)

a= Solution().search( [1], 0)
print(a)





# time and space complexity
# -------------------------
# time --> O(log n)
# space -> O(1)

# output
"""
array [4, 5, 6, 7, 0, 1, 2]
mid 3
 left sorted and target lies in opposite right side
low, high 4 6
mid 5
 left sorted and target lies in opposite right side
low, high 6 6
mid 6
 left sorted and target lies in opposite right side
low, high 7 6
-1


array [1]
mid 0
 left sorted and target lies in opposite right side
low, high 1 0
-1
"""