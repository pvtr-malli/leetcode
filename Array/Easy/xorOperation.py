# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 12:02:22 2020

@author: ninjaac
"""


"""
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

 

Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
"""
import functools
class Solution:
    def xorOperation(n,start):
        p = [start + 2*i for i in range(n)]
        
        return functools.reduce(lambda a,b :  a^b, p)
    
print(Solution.xorOperation(5,0))
        