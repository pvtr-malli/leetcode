"""
--problem--
-----------
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

--example--
-----------
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

--link--
--------
https://leetcode.com/problems/subsets/


complexity
-----------
MEDIMUM

"""

class Solution:
    def __init__(self):
        self.result = []
    def subsets(self, nums):
        def subset_rec(arr, i, subset, length):
            if i == length:
                self.result.append(subset.copy())
                return
            # pick the current index value
            subset.append(arr[i])
            subset_rec(arr, i+1, subset, length)
            subset.remove(arr[i])

            # not pick the current index value
            subset_rec(arr, i+1, subset, length)
        subset_rec(nums, 0, [], len(nums))
        return self.result


a = Solution().subsets([1,2,3])
print(a)


# print all subsets using recursion

def subsets(nums):
    result = []
    result.append([])
    # iterate over all the numbers in the array
    for num in nums:
        # add it to the subset list.
        for i in range(len(result)):
            result.append(result[i] + [num])
    print(result)


subsets([1,2,3])
# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""