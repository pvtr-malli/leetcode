"""
--problem--
-----------
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

--example--
-----------
Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

--link--
--------
https://leetcode.com/problems/combination-sum/


complexity
-----------
MEDIUM

"""

class Solution:
    def __init__(self) -> None:
        self.result = []
    def combinationSum(self, candidates, target):
        
        def combinationsum_rec(arr, ind, target, com):
            if ind == len(arr):
                return
            if target == 0:
                self.result.append(com.copy())
                return
            if arr[ind] <= target:
                # picking the current element
                com.append(arr[ind])
                combinationsum_rec(arr, ind, target-arr[ind], com)
                com.remove(arr[ind])

            # not picking the current element
            combinationsum_rec(arr, ind+1, target, com)
        combinationsum_rec(candidates, 0, target, [])
        return self.result

a = Solution().combinationSum([2,7,6,3,5,1], 9)
print(a)





# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""