"""
--problem--
-----------
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

--example--
-----------
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


--Constraints--
---------------
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104


--link--
--------
https://leetcode.com/problems/coin-change/


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
    def coinChange(self, coins, amount) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        a =  self.coinChange_rec(n-1, amount, coins)
        return a if a != 1e9 else -1

    def coinChange_rec(self, i, amount, coins):
        if i == 0:
            if (amount % coins[i]) == 0 :
                return amount // coins[i]
            else:
                return 1e9
        not_take = 0 + self.coinChange_rec(i-1, amount, coins)
        take = 1e9
        if coins[i] <= amount:
            take = 1 + self.coinChange_rec(i, amount- coins[i], coins)
        return min(not_take, take)
# time and space complexity
# -------------------------
# time --> O(2**n)[even more greater since we can take one coin multiple times](exponetial)
# space -> O(amount)[even more greater exponetial]


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================

    # step 2 :cheking the suproblem already solved or not.

    # step 3 : assign this sub problem ans to dp arrray.
# step 1 : define dp array.
# assihn one extra space and left '0' index unused-- easy to call the index.
class Solution:
    def coinChange(self, coins, amount) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        dp = []
        # step 1
        for i in range(n):
            dp.append([-1]*(amount+1))

        a = self.coinChange_rec(n-1, amount, coins, dp)
        return a if a != 1e9 else -1

    def coinChange_rec(self, i, amount, coins, dp):
        if i == 0:
            if (amount % coins[i]) == 0:
                return amount // coins[i]
            else:
                return 1e9
        # step 2
        if dp[i][amount] != -1 :
            return dp[i][amount]
        not_take = 0 + self.coinChange_rec(i-1, amount, coins, dp)
        take = 1e9
        if coins[i] <= amount:
            take = 1 + self.coinChange_rec(i, amount- coins[i], coins, dp)
        # step 3
        dp[i][amount] =  min(not_take, take)
        return dp[i][amount]

# time and space complexity
# -------------------------
# time --> O(n*amount)
# space ->O(n*amount)[dp] + O(amount)[axiloty]


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index.

    # ste 4: store the ans.
class Solution:
    def coinChange(self, coins, amount) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        dp = []
        # step 1
        for i in range(n):
            dp.append([0]*(amount+1))
        # step 2
        for i in range(amount+1):
            if (i % coins[0]) == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = 1e9
        # step 3
        for i in range(1,n):
            for amo in range(0, amount+1):
                # step 4
                not_take = 0 + dp[i-1][amo]
                take = 1e9
                if coins[i] <= amo:
                    take = 1 + dp[i][amo- coins[i]]
                dp[i][amo] = min(take,not_take)
        return dp[n-1][amount] if dp[n-1][amount] != 1e9 else -1

# time and space complexity
# -------------------------
# time --> O(n*amount)
# space ->O(n*amount)[dp] 


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
class Solution:
    def coinChange(self, coins, amount) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        # step 1
        prev = [0]*(amount+1)
        # step 2
        for i in range(amount+1):
            if (i % coins[0]) == 0:
                prev[i] = i // coins[0]
            else:
                prev[i] = 1e9
        # step 3
        for i in range(1,n):
            cur = [0]*(amount+1)
            # we are initializing values for only 0th index -- > no need to assign it to here.
            for amo in range(0, amount+1):
                # step 4
                not_take = 0 + prev[amo]
                take = 1e9
                if coins[i] <= amo:
                    take = 1 + cur[amo - coins[i]]
                cur[amo] = min(take,not_take)
            prev = cur
        return prev[amount] if prev[amount] != 1e9 else -1

# time and space complexity
# -------------------------
# time --> O(n*amount)
# space -> O(amount)*2 [prev,cur]




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


