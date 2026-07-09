"""
--problem--
-----------
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

--example--
-----------
Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1



--Constraints--
---------------
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000


--link--
--------
https://leetcode.com/problems/target-sum/


complexity
-----------
MEDIUM

"""

# SAME AS C0_8_5_PARTITION_WITH_GIVEN_FIFF -- NO SINGLE LINE OF CODE CHANGE -- JUST CALLING THAT FUNC
# all time and space complexities are same .
# all recursion, memoization,tabulation, memory optimization is same.

# Recurssion
# ==========================
# step 1: represent the problem as index.-- do base case 1) destiation 2) out of bound check
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem

# time and space complexity
# -------------------------
# time --> 
# space ->


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================

    # step 2 :cheking the suproblem already solved or not.

    # step 3 : assign this sub problem ans to dp arrray.
# step 1 : define dp array.
# assihn one extra space and left '0' index unused-- easy to call the index.

# time and space complexity
# -------------------------
# time --> 
# space ->


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index.

    # ste 4: store the ans.

class Solution:
    def findTargetSumWays(self, nums, target) -> int:
        return self.countPartitions(len(nums), target, nums)
    def countPartitions(n, d, arr) -> int:
        total_sum = sum(arr)
        # print(total_sum)
        if total_sum - d < 0:
            return 0
        if (total_sum - d ) % 2 != 0 : return 0
        target = (total_sum - d )//2
        # step 1:
        dp = []
        for i in range(n):
            dp.append([0]*(target+1))
        # step 2:
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
        # for i in range(n):
        #     dp[i][0] = 1
        if arr[0] != 0 and arr[0] <=target:
            dp[0][arr[0]] = 1
        # step 3:
        for i in range(1,n):
            for tar in range(0,target+1):

                # step 4
                not_take = dp[i-1][tar]
                take = 0
                if arr[i] <= tar:
                    take = dp[i-1][tar-arr[i]]
                dp[i][tar] = (take + not_take) 
                # print(take + not_take)
                # print(dp)
        return dp[n-1][target] 
# time and space complexity
# -------------------------
# time --> 
# space ->


# Memory optimization (optimize space we have in tabulation)
# ==========================================================


# time and space complexity
# -------------------------
# time --> 
# space ->




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


