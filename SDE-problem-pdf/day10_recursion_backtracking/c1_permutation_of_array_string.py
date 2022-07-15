"""
--problem--
-----------
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

--example--
-----------
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

--link--
--------
https://leetcode.com/problems/permutations/


complexity
-----------
MEDIUM

"""


class Solution:
    def __init__(self) -> None:
        self.result = []
    def permute(self, nums):
        def permute_rec(arr, i):
            if i == len(arr):
                self.result.append(arr.copy())
                return
            for ind in range(i, len(arr)):
                # swap the ind with i
                arr[ind], arr[i] = arr[i], arr[ind]
                permute_rec(arr, i+1)
                # backtracking
                # swap back the ind and i to get the arr to it's original position previous calling this function.
                arr[ind], arr[i] = arr[i], arr[ind]

        permute_rec(nums, 0)
        return self.result

a = Solution().permute([1,2,3])
print(a)
# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""