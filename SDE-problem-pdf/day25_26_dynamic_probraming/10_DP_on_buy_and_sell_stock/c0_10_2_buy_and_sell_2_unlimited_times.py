"""
--problem--
-----------
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

--example--
-----------
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.


--Constraints--
---------------
1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104


--link--
--------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


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
    def maxProfit(self, prices) -> int:
        return self.maxProfit_rec(0, 1, prices)
    def maxProfit_rec(self, i, can_buy, prices):
        if i == len(prices):
            return 0
        if can_buy == 1:
            buy = -prices[i] + self.maxProfit_rec(i + 1, 0, prices)
            not_buy = 0 + self.maxProfit_rec(i + 1, 1, prices)
            profit = max(buy, not_buy) # same as  max(-prices[i] + self.maxProfit_rec(i + 1, 0, prices), self.maxProfit_rec(i + 1, 1, prices))
        else:
            sell = prices[i] + self.maxProfit_rec(i + 1, 1, prices)
            not_sell = 0 + self.maxProfit_rec(i + 1, 0, prices)
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
    def maxProfit(self, prices) -> int:
        dp = []
        for i in range(len(prices)):
            dp.append([-1] * 2)
        return self.maxProfit_rec(0, 1, prices, dp)
    def maxProfit_rec(self, i, can_buy, prices, dp):
        if i == len(prices):
            return 0
        if dp[i][can_buy] != -1:
            return dp[i][can_buy]
        if can_buy == 1:
            buy = -prices[i] + self.maxProfit_rec(i + 1, 0, prices, dp)
            not_buy = 0 + self.maxProfit_rec(i + 1, 1, prices, dp)
            profit = max(buy, not_buy)
        else:
            sell = prices[i] + self.maxProfit_rec(i + 1, 1, prices, dp)
            not_sell = 0 + self.maxProfit_rec(i + 1, 0, prices, dp)
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
    def maxProfit(self, prices) -> int:
        n= len(prices)
        dp = []
        for i in range(len(prices) + 1):
            dp.append([0] * 2)

        # no base case since already everything zero.
        for i in range(n-1, -1, -1):
            for can_buy in range(1,-1,-1):
                if can_buy == 1:
                    buy = -prices[i] + dp[i+1][0]
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
    def maxProfit(self, prices) -> int:
        n= len(prices)
        prev = [0] * 2
        cur = [0] * 2
        # no base case since already everything zero.
        for i in range(n-1, -1, -1):
            for can_buy in range(1,-1,-1):
                if can_buy == 1:
                    buy = -prices[i] + prev[0]
                    not_buy = 0 + prev[1]
                    profit = max(buy, not_buy) # same as max(-prices[i] + prev[0], prev[1])
                else:
                    sell = prices[i] + prev[1]
                    not_sell = 0 + prev[0]
                    profit = max(sell, not_sell)
                cur[can_buy] = profit
            prev = cur
        return prev[0]
# time and space complexity
# -------------------------
# time --> O(n*2)
# space -> O(2) * 2



# we can optimize to 4 variables.

class Solution:
    def maxProfit(self, prices) -> int:
        n= len(prices)
        prev_buy = prev_not_buy = 0
        cur_buy= cur_not_buy = 0
        # no base case since already everything zero.
        for i in range(n-1, -1, -1):
            # if we had the for loop -- we will first but and then sell -- that what we do here.
            # we will defentely do the buy:
            buy = -prices[i] + prev_not_buy
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


