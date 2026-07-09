# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        low = mid = 0
        high = len(nums)-1
        while mid<=high:
            if nums[mid] == 0:
                """temp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = temp"""
                nums[low] , nums[mid] = 0 , nums[low]
                low+=1
                mid+=1
                print('0',nums)
            elif nums[mid]  == 1:
                mid+=1
                print('1',nums)
            elif nums[mid]  ==2:
                """temp = nums[high]
                nums[high] = nums[mid]
                nums[mid] = temp"""
                nums[high] , nums[mid] = 2 , nums[high]
                high-=1
                print('2',nums)
        
    
    
    
    
    
    
    
Solution().sortColors([2,0,1,1,0])