# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 23:46:26 2020

@author: ninjaac
"""
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d=dict()
        for i,n in enumerate(nums):
            d[n]=i
        print(d)
        for i,n in enumerate(nums):
            r=target-n
            if r in d:
                
                return [i,d[r]]
        
        
print(Solution().twoSum(nums=[3,2,4], target=6))

"""
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		tmp_map = {}
		for index, num in enumerate(nums):
			if  target - num in tmp_map:
				return [index, tmp_map[target - num]]
			tmp_map[num] = index
"""