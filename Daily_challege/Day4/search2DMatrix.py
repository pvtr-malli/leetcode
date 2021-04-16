# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:36:22 2021

@author: ELCOT
"""

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

1)Integers in each row are sorted from left to right.
2)The first integer of each row is greater than the last integer of the previous row.

"""
def binary_search(li , low , high , x):
    #print(li)
    mid = (low+high)//2
    if high>=low:
        if li[mid]==x:
            return 1
        elif li[mid]<x:
            return binary_search(li , mid+1 , high , x)
        elif li[mid]>x:
            return binary_search(li , low , mid-1 , x)
        
    else:
        return 0
    
class Solution:
    def searchMatrix(self , m , x):
        
            
        c = 0
        
        l = len(m)-1
        col = len(m[0])-1
        if l == 0 and col == 0:
            if m[0][0] == x:
                return True 
            return False
        while c<l:
            #print(c,n)
            if m[c][col] >= x:
                break
            else:
                c+=1
                
          
        b = binary_search(m[c] , 0 , len(m[c])-1 ,x )
        
        if b == 1:
            return True
        else:
            return False
        
        
Solution().searchMatrix([[1],[3]],1)