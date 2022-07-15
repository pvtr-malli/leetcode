"""
--problem--
-----------
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

--example--
-----------
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

--link--
--------
https://leetcode.com/problems/combination-sum-ii/


complexity
-----------
MADIUM

"""

class Solution:
    def __init__(self) -> None:
        self.result = []
    def combinationSum2(self, candidates, target):

        def combinationSum2_rec(arr, ind, ans, length, target):
            if target == 0:
                self.result.append(ans.copy())
                return
            if ind == length:
                #self.result.append(subset.copy())
                return

            for i in range(ind, length):
                if i!=ind and arr[i] == arr[i-1]:
                    continue
                if arr[i] > target:
                    break
                ans.append(arr[i])
                combinationSum2_rec(arr, i+1, ans,length, target-arr[i])
                ans.remove(arr[i])
        candidates = sorted(candidates)
        combinationSum2_rec(candidates, 0 , [], len(candidates),target)
        return self.result

a = Solution().combinationSum2([10,1,2,7,6,1,5], 8)
print(a)






# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""