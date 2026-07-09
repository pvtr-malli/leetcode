# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 08:39:12 2021

@author: ELCOT
"""
"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
 
"""
class Solution:
    def setZeroes(self, ma):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(ma)
        n = len(ma[0])
        
        for i in range(m):
            for j in range(n):
                if ma[i][j] == 0:
                    print('set the value to zero',i,j)
                    print('set the roe marker')
                    if ( ma[0][0]=='c' or ma[0 ][0] == 'rc' ) and i == 0:
                        ma[0][0] = 'rc'
                        print(ma)
                    else :
                        
                        ma[i][0] = 'r'
                        print(ma)
                    print('set the column marker')
                    if (ma[0][0]=='r' or ma[0][0]=='rc') and j==0: 
                        ma[0][0] = 'rc'
                        print(ma)
                    else: 
                        ma[0][j] = 'c'   
                        print(ma)
                    
                    
                    
                   
        print(ma)
        
        #set the value as '0' to do that only need to visit the first column and first row only
        #if it has '-1' then set that row and column to 0
        
        #to traver the column
        print('column traversal')
        for i in range(1):
            for j in range(1,n):
                #print(i,j)
                
                if ma[i][j] == 'c':
                    print(i,j)
                    for row in range(1,m): #levae the first row beacese it actng like a marker
                        print('row',row,j)
                        ma[row][j] = 0
        
        #travers the row to set it zero
        #print('row traversal')
        for i in range(m):
            for j in range(1):
                
                #print(i,j)
                #print(ma[i][j])
                if ma[i][j] == 'r':
                    for col in range(n):
                        #print(i,col)
                        ma[i][col] = 0
        print(ma)        
        if ma[0][0] == 'c':
            for row in range(1,m):
                ma[row][0] = 0        
        #handle the fort row 
        for i in range(1):
            for j in range(n):
                if ma[i][j] == 'c':
                    print('first row c')
                    ma[i][j] = 0
        print(ma)
        if ma[0][0] == 'rc':
            for col in range(n):
                ma[0][col] = 0
            for row in range(m):
                ma[row][0] = 0
        
            
        print(ma)
        

Solution().setZeroes([[1],[0],[3]])        


#[[0,1,2,0],[3,4,5,2],[1,3,1,5]]