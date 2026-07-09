# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 00:14:42 2020

@author: ninjaac
"""
"""
from collections import Counter
class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s):
        if s=="":
            return 0
        
        r,l,long=0,0,0
        lenth=len(s)
        if lenth==1:
            return 1
        while r<lenth:
            if max(Counter(s[l:r+1]).values())==1:
                
                r+=1
                print('r increse',r)
                print(s[l:r+1])
            else:
                l+=1
                print('l increse ',l)
                t=len(s[l:r+1])
                print(s[l:r+1])
                if t>long:
                    long=t
            
        return long
print(Solution().lengthOfLongestSubstring(s='auc'))
"""
from collections import Counter
class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s):
        if s=="":
            return 0
        
        r,l,long=0,0,0
        lenth=len(s)
        
        if lenth==1:
            return 1
        while r<lenth:
            if max(Counter(s[l:r+1]).values())!=1:
                l+=1
            r+=1
            if max(Counter(s[l:r+1]).values())==1:
                t=len(s[l:r+1])
                print(s[l:r+1])
                if t>long:
                    long=t
            
        return long
print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
"""
#the above code is for contiguous longeststring
#below is longest string
class Solution:
    def lengthOfLongestSubstring(self, seq: str) -> int:
        seen = {}
        leftP = 0
        output = 0
        for rightP, char in enumerate(seq):
            if char not in seen or seen[char] < leftP:
                output = max(output, rightP-leftP+1)
            else:
                leftP = seen[char]+1
            seen[char] = rightP
        return output
"""