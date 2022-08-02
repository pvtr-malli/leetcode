"""
--problem--
-----------
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

--example--
-----------
Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]


--Constraints--
---------------
1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.


--link--
--------
https://leetcode.com/problems/largest-divisible-subset/


complexity
-----------
MEDIUM

"""

# len and get the array  method
class Solution:
    def largestDivisibleSubset(self, nums):
        # n = len(nums)
        # nums = sorted(nums)
        # ans = []
        # length = 1
        # ans.append(nums[0])
        # for i in range(1,n):
        #     if nums[i] % ans[-1] == 0:
        #         # that is divisible -- we can add to ans
        #         ans.append(nums[i])
        #         length +=1 
        # return ans
        n = len(nums)
        nums = sorted(nums)
        maxi = 1
        dp = [1] * n
        hash_table = [0] * n
        last_index = 0
        for i in range(0,n):
            hash_table[i] = i
            for prev_i in range(0, i):
                if nums[i] % nums[prev_i] == 0 and dp[i] < 1+dp[prev_i]:
                    dp[i] = 1+dp[prev_i]
                    hash_table[i] = prev_i
            if dp[i] > maxi:
                maxi = dp[i]
                last_index = i
        # get the list 
        ans = []
        print(hash_table)
        print(dp)
        ans.append(nums[last_index])
        while last_index != hash_table[last_index]:
            last_index = hash_table[last_index]
            ans.append(nums[last_index])
        print(list(reversed(ans)))  

print(Solution().largestDivisibleSubset([1,2,4,8]))



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

        # step 4: Do what we need to do with the index. -- basically copy the recurence.

    # ste 4: store the ans.

# time and space complexity
# -------------------------
# time --> 
# space -> 


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
# always initalize the second array (cur) inside the for loop -- other wise gives some error.



# time and space complexity
# -------------------------
# time --> 
# space -> 



# output
"""

"""


