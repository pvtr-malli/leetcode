# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:18:17 2020

@author: ninjaac
"""


class Solution:
    @staticmethod
    def balancedStringSplit(s):
        bal,result=0,0
        l=len(s)
        for i in range(l):
            if s[i]=="R":
               bal+=1
            else:bal-=1
            if bal==0:
                result+=1
        return result
print(Solution().balancedStringSplit('LLRRRLLR'))