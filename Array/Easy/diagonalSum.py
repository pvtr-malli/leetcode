# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 16:46:40 2020

@author: ninjaac
"""
"""
 Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.   
"""
import numpy as np
class Solution:
    @staticmethod
    def diagonalSum(mat):
        l=len(mat)
        if l%2!=0:
            add = mat[(l//2)][(l//2)]
            m = np.array(mat)
            res=sum(m.diagonal())+sum(np.fliplr(m).diagonal())-add
        else:
            m = np.array(mat)
            res=sum(m.diagonal())+sum(np.fliplr(m).diagonal())
        return res
print(Solution.diagonalSum([[5]]))

print(Solution.diagonalSum([[1,2,3],
              [4,5,6],
              [7,8,9]]))


"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # corner case
        
        res = 0
        i,j = 0, len(mat[0])-1
        for nlist in mat:
            res += nlist[i]+nlist[j] if i!=j else nlist[i]
            i += 1
            j -= 1
        return res

"""