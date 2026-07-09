"""
--problem--
-----------
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

--example--
-----------
Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 


--Constraints--
---------------
0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000


--link--
--------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/


complexity
-----------
HARD

"""

# Recurssion
# ==========================
# step 1: represent the problem as index.-- do base case 1) destiation 2) out of bound check
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem
class Solution:
    def maxProfit(self, k, prices) -> int:
        return self.maxProfit_rec(0, 0, prices,k)
    def maxProfit_rec(self, i,n_trans, prices,k):
        if i == len(prices) or n_trans == 2*k:
            return 0
        if n_trans%2 == 0: # even buy
            buy = -prices[i] + self.maxProfit_rec(i + 1,n_trans +1, prices,k)# will be increase  when you are buying it.
            not_buy = 0 + self.maxProfit_rec(i +1, n_trans, prices,k)
            profit = max(buy, not_buy) 
        else:
            sell = prices[i] + self.maxProfit_rec(i + 1,n_trans+1, prices,k) # will be increase  when you are selling it.
            not_sell = 0 + self.maxProfit_rec(i + 1,n_trans, prices,k)
            profit = max(sell, not_sell)
        return profit

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
class Solution:
    def maxProfit(self,k, prices) -> int:
        n = len(prices)
        dp = []
        for i in range(n):
            dp.append([-1]*(2*k+1))

        return self.maxProfit_rec(0,0, prices, dp,k)
    def maxProfit_rec(self, i,n_trans, prices, dp,k):
        if i == len(prices) or n_trans == 2*k:
            return 0
        if dp[i][n_trans] != -1:
            return dp[i][n_trans]
        if n_trans%2 == 0: # even buy
            buy = -prices[i] + self.maxProfit_rec(i + 1,n_trans +1, prices, dp,k)# will be increase  when you are buying it.
            not_buy = 0 + self.maxProfit_rec(i +1, n_trans, prices, dp,k)
            profit = max(buy, not_buy) 
        else:
            sell = prices[i] + self.maxProfit_rec(i + 1,n_trans+1, prices, dp,k) # will be increase  when you are selling it.
            not_sell = 0 + self.maxProfit_rec(i + 1,n_trans, prices, dp,k)
            profit = max(sell, not_sell)
        dp[i][n_trans] =  profit
        return dp[i][n_trans]
# time and space complexity
# -------------------------
# time --> O(n*2k)
# space -> O(n*2k)[dp] + O(n)[axilory]


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index. -- basically copy the recurence.

    # ste 4: store the ans.
class Solution:
    def maxProfit(self,k, prices) -> int:
        n = len(prices)
        dp = []
        for i in range(n+1):
            dp.append([0]*(2*k+1))
        
        # base case assignment no need , since everything is zero.
        for i in range(n-1, -1, -1):
                for n_trans in range(2*k-1,-1,-1):
                    if n_trans%2 == 0:
                        buy = -prices[i] + dp[i+1][n_trans+1]
                        not_buy = dp[i+1][n_trans]
                        profit = max(buy, not_buy) 
                    else:
                        sell = prices[i] + dp[i+1][n_trans+1] 
                        not_sell = dp[i+1][n_trans]
                        profit = max(sell, not_sell)
                    dp[i][n_trans] =  profit

        return dp[0][0]
# time and space complexity
# -------------------------
# time --> O(n*2k)
# space -> O(n*2k)[dp]


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
# always initalize the second array (cur) inside the for loop -- other wise gives some error.
class Solution:
    def maxProfit(self,k, prices) -> int:
        n = len(prices)
        prev = [0]*(2*k+1)
        cur = [0]*(2*k+1)
        # base case assignment no need , since everything is zero.
        for i in range(n-1, -1, -1):
            for n_trans in range(2*k-1,-1,-1):
                if n_trans%2 == 0:
                    buy = -prices[i] + prev[n_trans+1]
                    not_buy = prev[n_trans]
                    profit = max(buy, not_buy) 
                else:
                    sell = prices[i] + prev[n_trans+1] 
                    not_sell = prev[n_trans]
                    profit = max(sell, not_sell)
                cur[n_trans] =  profit
            prev = cur
        return prev[0]
# time and space complexity
# -------------------------
# time --> O(n*2k)
# space -> O(2k) * 2




# 1D space optimized

class Solution:
    def maxProfit(self,k, prices) -> int:
        n = len(prices)
        cur = [0]*(2*k+1)
        # base case assignment no need , since everything is zero.
        for i in range(n-1, -1, -1):
            for n_trans in range(2*k-1,-1,-1):
                if n_trans%2 == 0:
                    buy = -prices[i] + cur[n_trans+1]
                    not_buy = cur[n_trans]
                    profit = max(buy, not_buy) 
                else:
                    sell = prices[i] + cur[n_trans+1] 
                    not_sell = cur[n_trans]
                    profit = max(sell, not_sell)
                cur[n_trans] =  profit
        return cur[0]
# output

# time and space complexity
# -------------------------
# time --> O(n*2k)
# space -> O(2k)
"""

"""


