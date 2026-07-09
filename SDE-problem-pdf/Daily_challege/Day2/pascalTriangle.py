# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 10:35:39 2021

@author: ELCOT
"""

"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]    
"""

class Solution:
    def generate(self,n):
        res = [[1]]
        if n == 1:
            return res
        
        for i in range(2,n+1):
            r = [1]
            for j in range(2,i):
                #print(i,j)
                
                
                s = (r[-1] * (i-(j-1))) / (j-1)
                r.append(int(s))
            r.append(1)
            res.append(r)
                
        print(res)       
Solution().generate(5)