# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 23:26:52 2020

@author: ninjaac
"""

#when using here dont sent the list slicinging to the recursive process becasues when doing like
#that it may create a new memory and store the slicing to the new memory so it will not affect the 
#original array 
import time
class Solution:
    @staticmethod
    def removeElement(nums,val):
        print(nums)
        for index,ele in enumerate(nums):
            print(index,ele)
            if ele == val: 
                nums.pop(index);print('deleted index,',index,ele)
                #Solution.removeElement(nums[index:],val)
                Solution.removeElement(nums,val)
                return nums
start=time.time()
print(Solution().removeElement(nums=[3,2,2,3,3,5,6,7],val=2))
end=time.time()
print(end-start)

"""class Solution:
    @staticmethod
    def removeElement(nums,val):
        
        index=0
        for i in range(0,len(nums)):
            if nums[index]==val: 
                nums.pop(index)
                
            else: 
                index+=1
        return nums
start=time.time()
print(Solution().removeElement(nums=[3,2,2,3,3,5,6,7],val=2))
end=time.time()
print(end-start)"""
