# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:59:38 2020

@author: ninjaac
"""


"""
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

 

Example 1:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
"""
class Solution:
    @staticmethod
    def createTargetArray(nums, index):
        n = len(nums);res = [0]*n
        for i in range(n):
            res[index[i]:]= [nums[i]] + res[index[i]:n-1]
            
        return res
print(Solution.createTargetArray(nums= [0,1,2,3,4], index = [0,1,2,2,1]))
        
        
        