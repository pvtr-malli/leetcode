# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 12:14:06 2020

@author: ninjaac
"""


"""Shuffle the array
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

    """

class Solution:
    def shuffle(nums,n):
        result=[]
        for a,b in zip(nums[0:n],nums[n:]):
            result.append(a)
            result.append(b)
        return result
        
        
Solution.shuffle([1,2,3,4,4,3,2,1],4)