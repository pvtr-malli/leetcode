# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:20:20 2021

@author: ELCOT
"""

class Solution:
    def nextPermutation(self, n):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l,index1,index2 = len(n),-1,-1
        for i in range(l-2 ,  -1 , -1):
            if n[i] < n[i+1]: 
                index1 = i
                break
        #print(index1)
        for i in range(l-1 ,-1  , -1):
            if n[index1] < n[i] :  
                index2 = i 
                break
        
        if index1!=-1 and index2!=-1:
            
            n[index1] , n[index2] = n[index2] , n[index1]
            
            n[index1+1 :] = n[-1 : (index1 - l) : -1]
            
        else:
            n[:] = n[::-1]
        
        
        #to get the even smaller number you can just reverse the number from index1 to last
        
        
        
        print(n)
Solution().nextPermutation([1,3,2])
