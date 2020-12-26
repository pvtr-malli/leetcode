# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 11:49:55 2020

@author: ninjaac
"""


"""Running Sum
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums


Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""

class Solution:
    @staticmethod
    def runningSum(nums):
        a = [sum(nums[0:i]) for i in range(1,len(nums)+1)]
        print(a)

Solution.runningSum([1,2,3,4])

import itertools
import functools
lis = [1,2,3,4]
# priting summation using accumulate() 
print ("The summation of list using accumulate is :",end="") 
print (list(itertools.accumulate(lis,lambda x,y : x+y)))

# priting summation using reduce() 
print ("The summation of list using reduce is :",end="") 
print (functools.reduce(lambda x,y:x+y,lis))  

print(functools.reduce(lambda a : a*2 if a>2 else a,lis))


print(list(filter(lambda a : True if a>=5 else False , [1,2,3,4,5])))
