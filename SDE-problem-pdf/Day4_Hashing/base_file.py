"""
--problem--
-----------
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

--example--
-----------
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

--link--
--------
https://leetcode.com/problems/subarray-sum-equals-k/
"""

# solution with two loop and no extra space.
# time --> O(n^2)
# space --> O(1)
class Solution:
    def subarraySum(self, nums, k):
        length = len(nums)
        count = 0
        i = 0
        while i < length:
            sum = nums[i]
            if sum == k:
                count +=1
            j = i+1
            while j < length:
                print("i",i,"j",j)
                sum += nums[j]
                print("sum", sum)
                if sum == k:
                    count += 1
                
                j+=1
            i+=1
        return count

a = Solution().subarraySum([1,2,3], 3)
print(a)

