# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 13:52:59 2021

@author: ELCOT
"""
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def maxSubArray(self,a):
        s , m = 0 , a[0]
        for i in a:
            if s<0: s = 0
            s+=i
            #print(s)
            if s>m: m = s
        return m
        
Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])