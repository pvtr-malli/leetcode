# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 16:43:38 2020

@author: ninjaac
"""


"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
"""

"""
The idea is using the int() to change the str binary to an integer number and then add those numbers 
after that using bin() convert those numbers to binary the returned value is in string formate

and like this _________'0b100' 

s=bin(10)
print(s.type()) // str

so remove the first 2 charecter we are using the replace()
"""

class Solution:
    @staticmethod
    def addBinary(a,b):
        return bin(int(a,2)+int(b,2))[2:] # when traversing to the whle list may take time so alternate solution
    

print(Solution().addBinary('1010', '1011'))


class Solution:
    @staticmethod
    def addBinary(a,b):
        return bin(int(a,2)+int(b,2)).replace('0b','')