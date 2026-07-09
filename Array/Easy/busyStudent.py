# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 22:57:38 2020

@author: ninjaac
"""


"""
Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

 

Example 1:

Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
Explanation: We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.
"""

class Solution:
    @staticmethod
    def busyStudent(startTime ,endTime ,queryTime):
        res = 0
        for i,j in zip(startTime,endTime):
            if i<=queryTime and j>=queryTime:
                res+=1
        return res
    
print(Solution.busyStudent([5], [5], 5))