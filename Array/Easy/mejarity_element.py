# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:51:25 2020

@author: ninjaac
"""


class Solution:
    @staticmethod
    def majorityElement(nums):
        result=[]
        sum=[]
        for i in nums:
            if i not in result:
                result.append(i)
        print(result)
        
        for index,ele in enumerate(result):
            count=0
            for a in nums:
                if(ele==a):count+=1; 
            sum.append(count)
            
        return result[sum.index(max(sum))]
print(Solution().majorityElement(nums=[2,2,1,1,1,2,2]))
            