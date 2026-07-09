# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 14:25:12 2021

@author: ELCOT
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == 2:
            return x*x
        
        
        isNeg = 0
        
        if n < 0:
            isNeg = 1       
        
        ans = self.helperfunc(x, abs(n))
        
        
        if isNeg:
            return 1/ans
        
        return ans
    
    # helper function to use divide and conquer DP strategy
    def helperfunc(self, num, p):
        if p == 1:
            return num 
        if p%2 == 0:
            return self.helperfunc(num , p//2) * self.helperfunc(num , p//2)
        else:
            print(num)
            return self.helperfunc(num , (p-1)//2) *  self.helperfunc(num , (p-1)//2) * num
        
        
        
        
Solution().myPow(0.00001,47)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def function(base = x, exponent = abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function()
        
        return float(f) if n >= 0 else 1/f
"""