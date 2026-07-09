# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:08:52 2020

@author: ninjaac
"""

"""
class Solution:
    @staticmethod
    def removeDuplicates(nums):
        
        count=0
        l= len(nums)
        
        if l==1:
            return 1
        for i in range(l-1):
            if (nums[i]==nums[i+1]):
                count+=1
                t=nums[i+1]
                nums[-1]=t
                print(nums)
        return l-count
        
print(Solution().removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))

class Solution:
    @staticmethod
    def removeDuplicates(nums):
        nums=set(nums)
        nums=list(nums)
        return len(nums)
print(Solution().removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))
"""
class Solution:
    @staticmethod
    def removeDuplicates(nums):
        
        index=0
        l= len(nums)        
        if l==1:
            return 1
        for i in range(l-1):
            if (nums[index]==nums[index+1]):
                print(index)
                nums.pop(index)
                print(nums)
            else:
                print('increasing the index')
                index+=1
print(Solution().removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))






        
        
        
        
        
        
    
