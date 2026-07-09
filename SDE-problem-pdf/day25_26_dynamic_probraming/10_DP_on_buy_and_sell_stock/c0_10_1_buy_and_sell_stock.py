"""
--problem--
-----------
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

--example--
-----------
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


--Constraints--
---------------
1 <= prices.length <= 105
0 <= prices[i] <= 104


--link--
--------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


complexity
-----------
EASY

"""


# no recursion -- simple for loop with min value remembering

class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        mini = prices[0]
        for i in range(1, len(prices)):
            cost = prices[i] - mini
            profit = max(profit, cost)
            # keeping the min value in memory -- so comes under DP
            mini = min(mini, prices[i])
        return profit

print(Solution().maxProfit([7,1,5,3,6,4]))
# time and space complexity
# -------------------------
# time -->  O(n)
# space -> O(1)

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




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


