"""
--problem--
-----------
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



--example--
-----------
Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


--Constraints--
---------------
1 <= prices.length <= 105
0 <= prices[i] <= 105


--link--
--------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/


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
    def maxProfit(self, prices) -> int:
        return self.maxProfit_rec(0, 1,2, prices)
    def maxProfit_rec(self, i, can_buy,n_trans, prices):
        if i == len(prices) or n_trans == 0:
            return 0
        if can_buy == 1:
            buy = -prices[i] + self.maxProfit_rec(i + 1, 0,n_trans, prices)
            not_buy = 0 + self.maxProfit_rec(i + 1, 1,n_trans, prices)
            profit = max(buy, not_buy) 
        else:
            sell = prices[i] + self.maxProfit_rec(i + 1, 1,n_trans-1, prices) # will be reduced only when you are selling it.
            not_sell = 0 + self.maxProfit_rec(i + 1, 0,n_trans, prices)
            profit = max(sell, not_sell)
        return profit
        

# time and space complexity
# -------------------------
# time --> O(2**n)[exponential]
# space -> O(n)


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================

    # step 2 :cheking the suproblem already solved or not.

    # step 3 : assign this sub problem ans to dp arrray.
# step 1 : define dp array.
# assihn one extra space and left '0' index unused-- easy to call the index.
class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        dp = []
        for i in range(n):
            a = []
            for b in range(2):
                a.append([-1]*3)
            dp.append(a)

        return self.maxProfit_rec(0, 1,2, prices, dp)
    def maxProfit_rec(self, i, can_buy,n_trans, prices, dp):
        if i == len(prices) or n_trans == 0:
            return 0
        if dp[i][can_buy][n_trans] != -1:
            return dp[i][can_buy][n_trans]
        if can_buy == 1:
            buy = -prices[i] + self.maxProfit_rec(i + 1, 0,n_trans, prices, dp)
            not_buy = 0 + self.maxProfit_rec(i + 1, 1,n_trans, prices, dp)
            profit = max(buy, not_buy) 
        else:
            sell = prices[i] + self.maxProfit_rec(i + 1, 1,n_trans-1, prices, dp) # will be reduced only when you are selling it.
            not_sell = 0 + self.maxProfit_rec(i + 1, 0,n_trans, prices, dp)
            profit = max(sell, not_sell)
        dp[i][can_buy][n_trans] =  profit
        return dp[i][can_buy][n_trans]
# time and space complexity
# -------------------------
# time --> O(n*2*3)
# space -> O(n*2*3)[dp] + O(n)[axilory]


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index. -- basically copy the recurence.

    # ste 4: store the ans.
class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        dp = []
        for i in range(n):
            a = []
            for b in range(2):
                a.append([0]*3)
            dp.append(a)
        
        # base case assignment no need , since everything is zero.
        for i in range(n-1, -1, -1):
            for can_buy in range(1, -1, -1):
                for n_trans in range(2,0,-1):
                    if can_buy == 1:
                        buy = -prices[i] + dp[i+1][0][n_trans]
                        not_buy = dp[i+1][1][n_trans]
                        profit = max(buy, not_buy) 
                    else:
                        sell = prices[i] + dp[i+1][1][n_trans-1] # will be reduced only when you are selling it.
                        not_sell = dp[i+1][0][n_trans]
                        profit = max(sell, not_sell)
                    dp[i][can_buy][n_trans] =  profit
        return dp[0][1][2]
# time and space complexity
# -------------------------
# time --> O(n*2*3)
# space -> O(n*2*3)[dp]


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
# always initalize the second array (cur) inside the for loop -- other wise gives some error.
class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        dp = []
        for i in range(n):
            a = []
            for b in range(2):
                a.append([-1]*3)
            dp.append(a)
        prev = []
        cur = []
        for b in range(2):
                prev.append([0]*3)
                cur.append([0]*3)
        # base case assignment no need , since everything is zero.
        for i in range(n-1, -1, -1):
            for can_buy in range(1, -1, -1):
                for n_trans in range(2,0,-1):
                    if can_buy == 1:
                        buy = -prices[i] + prev[0][n_trans]
                        not_buy = prev[1][n_trans]
                        profit = max(buy, not_buy) 
                    else:
                        sell = prices[i] + prev[1][n_trans-1] # will be reduced only when you are selling it.
                        not_sell = prev[0][n_trans]
                        profit = max(sell, not_sell)
                    cur[can_buy][n_trans] =  profit
            prev = cur
        return prev[1][2]
# time and space complexity
# -------------------------
# time --> O(n*2*3)
# space -> O(2*3) * 2












# we can do this using a 2 param also.


class Solution:
    def maxProfit(self, prices) -> int:
        return self.maxProfit_rec(0, 0, prices)
    def maxProfit_rec(self, i,n_trans, prices):
        if i == len(prices) or n_trans == 4:
            return 0
        if n_trans%2 == 0: # even buy
            buy = -prices[i] + self.maxProfit_rec(i + 1,n_trans +1, prices)# will be increase  when you are buying it.
            not_buy = 0 + self.maxProfit_rec(i +1, n_trans, prices)
            profit = max(buy, not_buy) 
        else:
            sell = prices[i] + self.maxProfit_rec(i + 1,n_trans+1, prices) # will be increase  when you are selling it.
            not_sell = 0 + self.maxProfit_rec(i + 1,n_trans, prices)
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
    def maxProfit(self, prices) -> int:
        n = len(prices)
        dp = []
        for i in range(n):
            dp.append([-1]*5)

        return self.maxProfit_rec(0,0, prices, dp)
    def maxProfit_rec(self, i,n_trans, prices, dp):
        if i == len(prices) or n_trans == 4:
            return 0
        if dp[i][n_trans] != -1:
            return dp[i][n_trans]
        if n_trans%2 == 0: # even buy
            buy = -prices[i] + self.maxProfit_rec(i + 1,n_trans +1, prices, dp)# will be increase  when you are buying it.
            not_buy = 0 + self.maxProfit_rec(i +1, n_trans, prices, dp)
            profit = max(buy, not_buy) 
        else:
            sell = prices[i] + self.maxProfit_rec(i + 1,n_trans+1, prices, dp) # will be increase  when you are selling it.
            not_sell = 0 + self.maxProfit_rec(i + 1,n_trans, prices, dp)
            profit = max(sell, not_sell)
        dp[i][n_trans] =  profit
        return dp[i][n_trans]
# time and space complexity
# -------------------------
# time --> O(n*4)
# space -> O(n*4)[dp] + O(n)[axilory]


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index. -- basically copy the recurence.

    # ste 4: store the ans.
class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        dp = []
        for i in range(n+1):
            dp.append([0]*5)
        
        # base case assignment no need , since everything is zero.
        for i in range(n-1, -1, -1):
                for n_trans in range(3,-1,-1):
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
# time --> O(n*4)
# space -> O(n*4)[dp]


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
# always initalize the second array (cur) inside the for loop -- other wise gives some error.
class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        prev = [0]*5
        cur = [0]*5
        # base case assignment no need , since everything is zero.
        for i in range(n-1, -1, -1):
            for n_trans in range(3,-1,-1):
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
# time --> O(n*4)
# space -> O(5) * 2




# 1D space optimized

class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        cur = [0]*5
        # base case assignment no need , since everything is zero.
        for i in range(n-1, -1, -1):
            for n_trans in range(3,-1,-1):
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
# time --> O(n*4)
# space -> O(5)
"""

"""


