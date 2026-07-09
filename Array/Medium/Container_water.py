# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 22:35:23 2020

@author: ninjaac
"""
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two
 endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains
 the most water.

Notice that you may not slant the container.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
################## hint
The aim is to maximize the area formed between the vertical lines. The area of any container is calculated using the shorter line as length and the distance between the lines as the width of the rectangle.
Area = length of shorter vertical line * distance between lines
We can definitely get the maximum width container as the outermost lines have the maximum distance between them. However, this container might not be the maximum in size as one of the vertical lines of this container could be really short.
"""

########### this solution take O(n2) time complexcity
"""
class Solution:
    @staticmethod
    def maxArea(height):
        l=len(height)
        
        curent_area=0
        
        for i in range(0,l):
            for j in range(i+1,l):
                print('ij',i,j)
                Area= min (height[i],height[j]) * (j-i)
                print(Area)
                if Area>curent_area:
                    curent_area=Area
        return curent_area
print(Solution().maxArea(height=[2,3,4,5,18,17,6]))
"""  
#another solution with 2 pointers

class Solution:
    @staticmethod
    def maxArea(height):
        
        area,i,j=0,0,len(height)-1
        while i<j:
            if height[i]<height[j]:
                area=max(height[i] * (j-i),area)
                i+=1
            else:
                area=max(height[j] * (j-i),area)
                j-=1
        return area
print(Solution().maxArea(height=[2,3,4,5,18,17,6]))

    