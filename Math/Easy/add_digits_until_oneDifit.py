# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 21:23:09 2020

@author: ninjaac
"""
"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution:
    @staticmethod
    def addDigits(num):
        if num<10:
            return num
        while not num<10:
            num=sum(int(ch) for ch in str(num))
        return num
        
print(Solution().addDigits(137))
        
        
"""
#best solution ever find this from discribtion
class Solution:
    def addDigits(self, num):
        if num < 10: return num
        if num % 9 == 0: return 9
        
        return num % 9
"""
