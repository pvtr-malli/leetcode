"""
--problem--
-----------
Given a non-empty array nums containing only positive integers,
 find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

--example--
-----------
Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.



--Constraints--
---------------
1 <= nums.length <= 200
1 <= nums[i] <= 100


--link--
--------
https://leetcode.com/problems/partition-equal-subset-sum/


complexity
-----------
MEDIUM

"""

# Recurssion
# ==========================
# step 1: represent the problem as index.
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem
class Solution:
    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        if total_sum %2 != 0 : # odd
            return False
        else:
            return self.subsetSumToK(len(nums), (total_sum//2), nums)
    def subsetSumToK(self, n, k, arr):

        # Write your code here
        # Return a boolean variable 'True' or 'False' denoting the answer
        return self.subsetSumToK_rec(n-1, k,arr)

    def subsetSumToK_rec(self,i, k, arr):
        if k == 0:
            return True
        if i ==0:
            return arr[0] == k
        take = False
        if arr[i] <= k:
            take = self.subsetSumToK_rec(i-1, k-arr[i], arr)
        not_take = self.subsetSumToK_rec(i-1, k , arr)
        return take or not_take

print(Solution().canPartition(4,5, [4,3,2,1]))


# time and space complexity
# -------------------------
# time --> O(2**n)[for each arra index we have two path(take or not take)]+ O(n)[sum calculation]
# space -> O(n)[axilory]


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================

    # step 2 :cheking the suproblem already solved or not.

    # step 3 : assign this sub problem ans to dp arrray.
# step 1 : define dp array.that shuld have all the variable things in the function call.
# assihn one extra space and left '0' index unused-- easy to call the index.
class Solution:
    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        if total_sum %2 != 0 : # odd
            return False
        else:
            return self.subsetSumToK(len(nums), (total_sum//2), nums)
    def subsetSumToK(self,n, k, arr):

        # Write your code here
        # Return a boolean variable 'True' or 'False' denoting the answer
        # step 1:
        dp = []
        for i in range(n):
            dp.append([-1]*(k+1))
        # print(dp)
        return self.subsetSumToK_rec(n-1, k,arr, dp)

    def subsetSumToK_rec(self,i, k, arr, dp):
        if k == 0:
            return True
        if i ==0:
            return arr[0] == k
        # step 3:
        if dp[i][k] != -1:
            return dp[i][k]
        take = False
        if arr[i] <= k:
            take = self.subsetSumToK_rec(i-1, k-arr[i], arr, dp)
        not_take = self.subsetSumToK_rec(i-1, k , arr, dp)
        # step2:
        dp[i][k] =  take or not_take
        return dp[i][k]
print(Solution().canPartition(4,5, [4,3,2,1]))
# time and space complexity
# -------------------------
# time --> O(n*target) # we have n*target ==> states + O(n)[sum calculation]
# space -> O(n*target)[dp] + O(n)[axilory]


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index.

    # ste 4: store the ans.
class Solution:
    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        if total_sum %2 != 0 : # odd
            return False
        else:
            return self.subsetSumToK(len(nums), (total_sum//2), nums)
    def subsetSumToK(self,n, k, arr):

        # Write your code here
        # Return a boolean variable 'True' or 'False' denoting the answer
        # step 1:
        dp = []
        for i in range(n):
            dp.append([False]*(k+1))
        # step 2:
        for i in range(n):
            dp[i][0] = True
        if arr[0]<=k:
            dp[0][arr[0]] = True
        # step 3:
        for i in range(1,n):
            for tar in range(1,k+1):
                print(i,tar)
                # step 4
                not_take = dp[i-1][tar]
                take = False
                if arr[i] <= tar:
                    take = dp[i-1][tar-arr[i]]
                dp[i][tar] = take or not_take
                print(take or not_take)
                print(dp)
        return dp[n-1][k] 
print(Solution().canPartition(4,5, [4,3,2,1]))

# time and space complexity
# -------------------------
# time --> O(n*target)+ O(n)[sum calculation]
# space -> O(n*target)


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
class Solution:
    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        if total_sum %2 != 0 : # odd
            return False
        else:
            return self.subsetSumToK(len(nums), (total_sum//2), nums)
    def subsetSumToK(self,n, k, arr):

        # Write your code here
        # Return a boolean variable 'True' or 'False' denoting the answer
        # step 1:
        prev = [False] * (k+1)
        
        # step 2:
        prev[0] = True
        if arr[0]<=k:
            prev[arr[0]] = True
        # step 3:
        for i in range(1,n):
            cur = [False] * (k+1)
            cur[0] = True
            for tar in range(1,k+1):
                # step 4
                not_take = prev[tar]
                take = False
                if arr[i] <= tar:
                    take = prev[tar-arr[i]]
                cur[tar] = take or not_take
            prev = cur
        return prev[k] 
print(Solution().canPartition(4,5, [4,3,2,1]))

# time and space complexity
# -------------------------
# time --> O(n*target)+ O(n)[sum calculation]
# space -> O(1)




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


