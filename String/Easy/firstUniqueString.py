# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:57:42 2020

@author: ninjaac
"""

"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
"""
from collections import Counter
class Solution:
    @staticmethod
    def firstUniqChar(s):
        if s=="":
            return -1
        if s==" ":
            return -1
        freq=Counter(s)
        print(freq.items())
        for let,c in freq.items():
            if c==1:
                return s.index(let)
        return -1
 
print(Solution().firstUniqChar(s='leedcode'))           