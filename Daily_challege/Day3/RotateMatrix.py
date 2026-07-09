# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:13:50 2021

@author: ELCOT
"""

class Solution:
    def rotate(self, m):
        """
        Do not return anything, modify matrix in-place instead.
        """
        #transpose the matrix
        row  = len(m) 
        for i in range(row):
            for j in range(i):
                print(i,j)
                m[i][j] , m[j][i] = m[j][i] , m[i][j]
            print(m)
        #reverse the each row elements
        for i in range(row):
            m[i] = m[i][::-1]
        print(m)
                
            
        
        
Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])