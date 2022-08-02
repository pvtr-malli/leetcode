"""
--problem--
-----------
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

--example--
-----------
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


--Constraints--
---------------
1 <= nums.length <= 2500
-104 <= nums[i] <= 104


--link--
--------
https://leetcode.com/problems/longest-increasing-subsequence/


complexity
-----------
MEDIUM

"""

# Recurssion
# ==========================
# step 1: represent the problem as index.-- do base case 1) destiation 2) out of bound check
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem

class Solution:
    def lengthOfLIS(self, nums) -> int:
        return self.lengthOfLIS_rec(0 , -1, nums)
    def lengthOfLIS_rec(self, i, prev_i, nums):
        if i == len(nums):
            return 0
        not_pick = 0 + self.lengthOfLIS_rec(i+1, prev_i, nums)
        pick=0
        if nums[i] > nums[prev_i] or prev_i == -1:
            pick = 1 + self.lengthOfLIS_rec(i+1, i, nums)
        return max(pick,not_pick)

# time and space complexity
# -------------------------
# time --> O(n**2)[exponetial]
# space -> O(n)[axilory]


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================

    # step 2 :cheking the suproblem already solved or not.

    # step 3 : assign this sub problem ans to dp arrray.
# step 1 : define dp array.
# assihn one extra space and left '0' index unused-- easy to call the index.
class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = []
        for i in range(len(nums)):
            dp.append([-1]* (len(nums)+1))
        return self.lengthOfLIS_rec(0 , -1, nums, dp)
    def lengthOfLIS_rec(self, i, prev_i, nums, dp):
        if i == len(nums):
            return 0
        if dp[i][prev_i+1] != -1:
            return dp[i][prev_i+1]
        not_pick = 0 + self.lengthOfLIS_rec(i+1, prev_i, nums, dp)
        pick=0
        if nums[i] > nums[prev_i] or prev_i == -1:
            pick = 1 + self.lengthOfLIS_rec(i+1, i, nums, dp)
        dp[i][prev_i+1] =  max(pick,not_pick)
        print(dp)
        return dp[i][prev_i+1]
# time and space complexity
# -------------------------
# time --> O(n**2)
# space -> O(n**2) + O(n)[axilory]


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index. -- basically copy the recurence.

    # ste 4: store the ans.
class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = []
        for i in range(len(nums)+1):
            dp.append([0]* (len(nums)+1))
        
        for i in range(n-1, -1,-1):
            for prev_i in range(i-1, -2, -1): #i-1 -- > -1
                not_pick = dp[i+1][prev_i+1]
                pick = 0
                if nums[i] > nums[prev_i] or prev_i == -1:
                    pick = 1 + dp[i+1][i+1]
                dp[i][prev_i+1] =  max(pick,not_pick)

        return dp[0][-1+1]
# time and space complexity
# -------------------------
# time --> O(n**2)
# space -> O(n**2)


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
# always initalize the second array (cur) inside the for loop -- other wise gives some error.

class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        prev = [0] * (n+1)
        cur = [0] * (n+1)
        for i in range(n-1, -1,-1):
            for prev_i in range(i-1, -2, -1): #i-1 -- > -1
                not_pick = prev[prev_i+1]
                pick = 0
                if nums[i] > nums[prev_i] or prev_i == -1:
                    pick = 1 + prev[i+1]
                cur[prev_i+1] =  max(pick,not_pick)
            prev = cur
        return prev[-1+1]

# time and space complexity
# -------------------------
# time --> O(n**2)
# space -> O(n)*2



# ANOTHER TABULATION ALGO METHOD --  NEED TO UNDERSTAND THIS



class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        maxi = 1
        dp = [1] * n
        for i in range(0,n):
            for prev_i in range(0, i):
                if nums[prev_i] < nums[i]:
                    dp[i] = max(dp[i], 1+dp[prev_i])
                    maxi = max(maxi, dp[i])
        return maxi

# time and space complexity
# -------------------------
# time --> O(n**2)[not exactly n**2 less than that]
# space -> O(n)



# prin the LIS

class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        maxi = 1
        last_index = 0
        dp = [1] * n
        hash_table = [0] * n

        for i in range(0,n):
            hash_table[i] = i # update with default index
            for prev_i in range(0, i):
                if nums[prev_i] < nums[i] and dp[i] < 1+dp[prev_i]:
                    dp[i] = 1+dp[prev_i]
                    hash_table[i] = prev_i
            if dp[i] > maxi:
                maxi = dp[i]
                last_index = i

        # print it.
        ans = []
        print(hash_table)
        ans.append(nums[last_index])
        while last_index != hash_table[last_index]:
            last_index = hash_table[last_index]
            ans.append(nums[last_index])
        print(list(reversed(ans)))  

Solution().lengthOfLIS([10,9,2,5,3,7,101,18])

# output
"""

"""


