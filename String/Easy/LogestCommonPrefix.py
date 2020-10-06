# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:25:29 2020

@author: ninjaac
"""
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
"""
"""
l=["flower","flow","flight"]
m=min(l)
print(m)
for i in l:
    print('i',i)

    v=''
    if m!=i:
        
        for i,j in zip(m,i):
            print('ij',i,j)
            if i==j:
                v+=i
                print('v',v)
            else:
                break
        m=v
    if m==' ':
        break
        
        print('mc',m)
print(m)
"""  

class Solution:
    @staticmethod
    def longestCommonPrefix(strs):
        if strs==[]:
            return ''
        m=min(strs)
        for i in strs:
            v=''
            if m!=i:
                for i,j in zip(m,i):
            
                    if i==j:
                        v+=i
                
                    else:
                        break
                m=v
            if m=='':
                break
            
        return m
print(Solution().longestCommonPrefix(strs=[]))
            
        