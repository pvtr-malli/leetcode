# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 12:56:35 2020

@author: ninjaac
"""


"""
Given an array nums of integers, return how many of them contain an even number of digits.
 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
"""
class Solution:
    @staticmethod
    def findNumbers(nums):
        
        res=[1 if len(str(i))%2 == 0 else 0 for i in nums]
        return sum(res)
        
    
print(Solution.findNumbers([12,345,2,5,7896]))


class Solution:
    @staticmethod
    def findNumbers(nums):
        res = 0
        for i in nums:
            if len(str(i))%2==0: res +=1
        return res
    
print(Solution.findNumbers([12,345,2,5,7896]))