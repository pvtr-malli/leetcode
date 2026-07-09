# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 23:12:08 2020

@author: ninjaac
"""
"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
"""
class Solution:
    @staticmethod
    def sumZero(n):
        res = []
        
        for i in range(1,(n//2)+1):
                res.append(i)
                res.append(-i)
        if n%2==0: return res
        res.append(0)               
        return res
print(Solution.sumZero(4))
