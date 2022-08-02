"""
--problem--
-----------
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

--example--
-----------
Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6


--Constraints--
---------------
1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104


--link--
--------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/


complexity
-----------
MEDIUm

"""


# Recurssion
# ==========================
# step 1: represent the problem as index.-- do base case 1) destiation 2) out of bound check
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem

class Solution:
    def maxProfit(self, prices, fee) -> int:
        return self.maxProfit_rec(0, 1, prices, fee)
    def maxProfit_rec(self, i, can_buy, prices, fee):
        if i == len(prices):
            return 0
        if can_buy == 1:
            buy = -prices[i] + self.maxProfit_rec(i + 1, 0, prices, fee) - fee
            not_buy = 0 + self.maxProfit_rec(i + 1, 1, prices, fee)
            profit = max(buy, not_buy) # same as  max(-prices[i] + self.maxProfit_rec(i + 1, 0, prices), self.maxProfit_rec(i + 1, 1, prices))
        else:
            sell = prices[i] + self.maxProfit_rec(i + 1, 1, prices, fee)
            not_sell = 0 + self.maxProfit_rec(i + 1, 0, prices, fee)
            profit = max(sell, not_sell)
        return profit

# time and space complexity
# -------------------------
# time --> O(2**n)[exponential]
# space -> O(n)[exponential]


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================

    # step 2 :cheking the suproblem already solved or not.

    # step 3 : assign this sub problem ans to dp arrray.
# step 1 : define dp array.
# assihn one extra space and left '0' index unused-- easy to call the index.

class Solution:
    def maxProfit(self, prices, fee) -> int:
        dp = []
        for i in range(len(prices)):
            dp.append([-1] * 2)
        return self.maxProfit_rec(0, 1, prices, dp, fee)
    def maxProfit_rec(self, i, can_buy, prices, dp, fee):
        if i == len(prices):
            return 0
        if dp[i][can_buy] != -1:
            return dp[i][can_buy]
        if can_buy == 1:
            buy = (-prices[i] + self.maxProfit_rec(i + 1, 0, prices, dp, fee)) - fee
            not_buy = 0 + self.maxProfit_rec(i + 1, 1, prices, dp, fee)
            profit = max(buy, not_buy)
        else:
            sell = prices[i] + self.maxProfit_rec(i + 1, 1, prices, dp, fee)
            not_sell = 0 + self.maxProfit_rec(i + 1, 0, prices, dp, fee)
            profit = max(sell, not_sell)
        dp[i][can_buy] =  profit
        return dp[i][can_buy]
# time and space complexity
# -------------------------
# time --> O(n*2)
# space -> O(n*2) + O(n)[axilory]


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index. -- basically copy the recurence.

    # ste 4: store the ans.

class Solution:
    def maxProfit(self, prices, fee) -> int:
        n= len(prices)
        dp = []
        for i in range(len(prices) + 1):
            dp.append([0] * 2)

        # no base case since already everything zero.
        for i in range(n-1, -1, -1):
            for can_buy in range(1,-1,-1):
                if can_buy == 1:
                    buy = -prices[i] + dp[i+1][0] - fee
                    not_buy = 0 + dp[i+1][1]
                    profit = max(buy, not_buy)
                else:
                    sell = prices[i] + dp[i+1][1]
                    not_sell = 0 + dp[i+1][0]
                    profit = max(sell, not_sell)
                dp[i][can_buy] = profit
        return dp[0][1]

print(Solution().maxProfit([7,1,5,3,6,4]))
# time and space complexity
# -------------------------
# time -->  O(n*2)
# space -> O(n*2)


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
# always initalize the second array (cur) inside the for loop -- other wise gives some error.
class Solution:
    def maxProfit(self, prices, fee) -> int:
        n= len(prices)
        prev = [0] * 2
        cur = [0] * 2
        # no base case since already everything zero.
        for i in range(n-1, -1, -1):
            for can_buy in range(1,-1,-1):
                if can_buy == 1:
                    buy = -prices[i] + prev[0] - fee
                    not_buy = 0 + prev[1]
                    profit = max(buy, not_buy) # same as max(-prices[i] + prev[0], prev[1])
                else:
                    sell = prices[i] + prev[1]
                    not_sell = 0 + prev[0]
                    profit = max(sell, not_sell)
                cur[can_buy] = profit
            prev = cur
        return prev[1]
# time and space complexity
# -------------------------
# time --> O(n*2)
# space -> O(2) * 2



# we can optimize to 4 variables.

class Solution:
    def maxProfit(self, prices, fee) -> int:
        n= len(prices)
        prev_buy = prev_not_buy = 0
        cur_buy= cur_not_buy = 0
        # no base case since already everything zero.
        for i in range(n-1, -1, -1):
            # if we had the for loop -- we will first but and then sell -- that what we do here.
            # we will defentely do the buy:
            buy = -prices[i] + prev_not_buy - fee
            not_buy = 0 + prev_buy
            cur_buy = max(buy, not_buy)
            # we will do the sell now itself.
            sell = prices[i] + prev_buy
            not_sell = 0 + prev_not_buy
            cur_not_buy = max(sell, not_sell)

            # chance the variable.
            prev_buy = cur_buy
            prev_not_buy = cur_not_buy
        return prev_buy

# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(1) * 4



# output
"""

"""


