"""
--problem--
-----------
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

--example--
-----------
Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]


--link--
--------
https://leetcode.com/problems/subsets-ii/


complexity
-----------
MEDIUM

"""

class Solution:
    def __init__(self) -> None:
        self.result = []
    def subsetsWithDup(self, nums):

        def subsetwithdub_rec(arr, ind, subset, length):
            self.result.append(subset.copy())
            if ind == length:
                #self.result.append(subset.copy())
                return
            for i in range(ind, length):
                if i!=ind and arr[i] == arr[i-1]:
                    continue
                subset.append(arr[i])
                subsetwithdub_rec(arr, i+1, subset,length)
                subset.remove(arr[i])
        nums = sorted(nums)
        subsetwithdub_rec(nums, 0 , [], len(nums))
        return self.result

a = Solution().subsetsWithDup([4,4,4,1,4])
print(a)










# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""