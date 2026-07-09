# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 23:22:23 2020

@author: ninjaac
"""

"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""
class Solution:
    @staticmethod
    def sortArrayByParity(A):
        o,e = [],[]
        for i in A:
            if i%2==0:o.append(i)
            else: e.append(i)
        return o+e
    
print(Solution.sortArrayByParity([3,1,2,4]))
