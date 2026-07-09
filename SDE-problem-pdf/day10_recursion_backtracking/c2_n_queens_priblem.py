"""
--problem--
-----------
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

--example--
-----------
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]

--link--
--------
https://leetcode.com/problems/n-queens/


complexity
-----------
HARD

"""


from copy import deepcopy

class Solution:
    def __init__(self) -> None:
        self.result = []
    def solveNQueens(self, n):
        def solve_rec(arr, n, col, leftarray, upperdiagonal, lowerdiagonal):
            if col == n:
                self.result.append(deepcopy(arr))
                return

            for r in range(0,n):
                if leftarray[r] == 0 and upperdiagonal[n-1 + (col - r)] == 0 and lowerdiagonal[r+ col] == 0:
                    arr[r][col] = "Q"
                    leftarray[r] = 1
                    upperdiagonal[n-1 + (col - r)] = 1
                    lowerdiagonal[r+col] = 1

                    # recursion
                    solve_rec(arr, n, col+1, leftarray, upperdiagonal, lowerdiagonal)

                    # backtracking
                    arr[r][col] = "."
                    leftarray[r] = 0
                    upperdiagonal[n-1 + (col - r)] = 0
                    lowerdiagonal[r+col] = 0
        
        arr = []
        for i in range(0,n):
            a = []
            for j in range(0,n):
                a.append(".")
            arr.append(a)
        leftarray = [0] * n 
        upperdiagonal = [0] * (2 * n +1)
        lowerdiagonal = [0] * (2 * n +1)
        solve_rec(arr, n, 0, leftarray, upperdiagonal, lowerdiagonal)

        # chage the result format
        res =[]
        for a in self.result:
            r =[]
            for single_a in a:
                r.append("".join(single_a))
            res.append(r)
        

        return res

a = Solution().solveNQueens(4)
print(a)


# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""