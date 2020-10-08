# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:24:44 2020

@author: ninjaac
"""

class Solution:
    @staticmethod
    def reverseVowels(s):
        if s==' ' or s=='':
            return ' '
        s=list(s)
        #print(s)
        i,j,vawel,=0,len(s)-1,['a','e','i','o','u']
        while i <j:
            if s[i] not in vawel: 
                #print(s[i])
                i+=1
            if s[j] not in vawel: 
                #print(s[j])
                j-=1
            if s[i] in vawel and s[j] in vawel:
                #print(s[i],s[j])
                temp=s[i]
                s[i]=s[j]
                s[j]=temp
                i+=1
                j-=1
        return ''.join(s)   
        
print(Solution().reverseVowels('leetcode'))