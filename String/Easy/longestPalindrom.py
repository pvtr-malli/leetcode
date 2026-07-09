# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:16:14 2020

@author: ninjaac
"""
"""
longest palindrom concept is very simple only odd numbers make palindrom and the even number of 
words make the palindrom so base don the 2 idea make this program
"""
from collections import Counter
class Solution:
    @staticmethod
    def longestPalindrome(s) :
        
        result = 0        
        freq = Counter(s)
        
        oddFlag = False
        
        for index,val in freq.items():
             if val%2==0:
                 result+=val
             else: 
                 oddFlag=True
                 result+=(val-1)
                 
        return (result+1) if oddFlag else result
print(Solution().longestPalindrome('aA'))