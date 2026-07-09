# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:07:42 2021

@author: ELCOT
"""

class Solution:
    def maxProfit(self, prices):
        buy = 1000000000
        profit = 0
        for i in prices:
            if i<buy:
                buy = i
            profit_ = i - buy
            if profit_>profit:
                profit = profit_
        return profit

Solution().maxProfit([7,1,5,3,6,4])        