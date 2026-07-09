# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 12:09:27 2020

@author: ninjaac
"""


"""
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

 

Example 1:

Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
"""

class Solution:
    def countGoodTriplets(arr,a,b,c):
        res = 0;l = len(arr)
        print(arr)
        for i in range(0,l):
            for j in range(i+1 , l):
                for k in range(j+1,l):
                    
                    if (abs(arr[i]-arr[j]) <=a) and (abs(arr[j]-arr[k] )<=b) and (abs(arr[i]-arr[k]) <=c):
                        res+=1
                        
        return res
    
print(Solution.countGoodTriplets([3,0,1,1,9,7],7,2,3))