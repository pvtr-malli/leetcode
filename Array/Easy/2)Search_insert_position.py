# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:12:58 2020

@author: ninjaac
"""


class Solution:
    @staticmethod
    def searchInsert(nums, target):
        for index,num in enumerate(nums):
            if num >= target:
                return index
        return len(nums)
                
        

print(Solution().searchInsert( nums=[1,3,5,6],target= 5))     

#time complexicity O(n) seraching the n values based on the target value
"""
#another solution
class Solution:
    @staticmethod
    def searchInsert(nums, target):
        for index in range(len(nums)):
            if nums[index]>= target:
                return index
        return len(nums)
                
print(Solution().searchInsert( nums=[1,3,5,6],target= 5))         


#another solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            else:
                if target<nums[i] and target>nums[i-1]:
                    return i
                elif target>nums[-1]:
                    return len(nums)
                elif target<nums[0]:
                    return 0
""" 
   