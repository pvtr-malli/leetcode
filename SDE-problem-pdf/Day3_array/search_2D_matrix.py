"""
-- problem -- 
-------------
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

--example--
-----------
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""



class Solution:
    def binary_search(self, arr, x):
        low = 0
        high = len(arr) - 1
        mid = 0
    
        while low <= high:
    
            mid = (high + low) // 2
    
            # If x is greater, ignore left half
            if arr[mid] < x:
                low = mid + 1
    
            # If x is smaller, ignore right half
            elif arr[mid] > x:
                high = mid - 1
    
            # means x is present at mid
            else:
                return True
    
        # If we reach here, then the element was not present
        return False
    def searchMatrix(self, matrix, target):
        row,col= len(matrix), len(matrix[0])
        
        target_row = 0
        for r in range(row):
            if matrix[r][col-1] >= target:
                target_row = r
                break
        print(target_row)
        print(matrix[target_row])
        return self.binary_search(matrix[target_row], target)

a = Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 16)
print(a)
a = Solution().searchMatrix(matrix = [[1],[3]], target = 1)
print(a)