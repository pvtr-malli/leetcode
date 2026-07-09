"""
--problem--
-----------
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

--example--
-----------

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10

--Constraints--
---------------
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104


--link--
--------

https://leetcode.com/problems/triangle/

complexity
-----------
MEDIUM

"""

# Recurssion
# =========================
# step 1: represent the problem as index.
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem
class Solution:
    def minimumTotal(self, triangle) -> int:
        return self.minimumTotal_rec(0,0 ,triangle)
    def minimumTotal_rec(self, i, j , triangle):
        n = len(triangle)
        if i == n-1:
            return triangle[i][j]
        down = triangle[i][j] + self.minimumTotal_rec(i+1, j , triangle)
        diagonal = triangle[i][j] + self.minimumTotal_rec(i+1, j+1 , triangle)
        return min(down, diagonal)

# time and space complexity
# -------------------------
# time --> 
# space -> O(n)[axilory]


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================

    

    
# step 1 : define dp array.
# assihn one extra space and left '0' index unused-- easy to call the index.
class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        m = len(triangle[-1]) # the last line has the higest num of ele.
        dp = []
        for row in range(n):
            dp.append([-1]*(m+1))
        return self.minimumTotal_rec(0,0 ,triangle, dp)
    def minimumTotal_rec(self, i, j , triangle,dp):
        n = len(triangle)
        if i == n-1:
            return triangle[i][j]
        # step 2 :cheking the suproblem already solved or not.
        if dp[i][j] != -1:
            return dp[i][j]
        down = triangle[i][j] + self.minimumTotal_rec(i+1, j , triangle, dp)
        diagonal = triangle[i][j] + self.minimumTotal_rec(i+1, j+1 , triangle, dp)
        # step 3 : assign this sub problem ans to dp arrray.
        dp[i][j] = min(down, diagonal)
        return dp[i][j]
# time and space complexity
# -------------------------
# time --> O(n*n)
# space -> O(n*n)[dp] + O(n)[axilory]


# Tabulation(base/down - top)  -- here doing n-1 - 0 (top - down)
# ==========================
class Solution:
    def minimumTotal(self, triangle) -> int:
        # step 1: define the same dp size dp array.
            n = len(triangle)
            m = len(triangle[-1]) # the last line has the higest num of ele.
            dp = []
            for row in range(n):
                dp.append([-1]*(m))
            # step 2: assign the values of base cases.
            for j in range(n):
                dp[n-1][j] = triangle[n-1][j]
            # step 3: Find which index to which index we need to travers and do the for loop.
            # careful about the index -- leave the base case index -- since that is already filled
            for i in range(n-2, -1, -1):
                for j in range(i, -1, -1):
                    # step 4: Do what we need to do with the index.
                    down = triangle[i][j] + dp[i+1][j]
                    diagonal = triangle[i][j] + dp[i+1][j+1]
                    # step 3 : assign this sub problem ans to dp arrray.
                    dp[i][j] = min(down, diagonal)
            return dp[0][0]
    # ste 5: store the ans.
print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
# time and space complexity
# -------------------------
# time --> O(n*n)
# space -> O(n*n)


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
class Solution:
    def minimumTotal(self, triangle) -> int:
        # step 1: define the same dp size dp array.
            n = len(triangle)
            m = len(triangle[-1]) # the last line has the higest num of ele.
            front = [-1] * n 
            # step 2: assign the values of base cases.
            for j in range(n):
                front[j] = triangle[n-1][j]
            # step 3: Find which index to which index we need to travers and do the for loop.
            # careful about the index -- leave the base case index -- since that is already filled
            for i in range(n-2, -1, -1):
                cur = [-1] *n
                for j in range(i, -1, -1):
                    # step 4: Do what we need to do with the index.
                    down = triangle[i][j] + front[j]
                    diagonal = triangle[i][j] + front[j+1]
                    # step 3 : assign this sub problem ans to dp arrray.
                    cur[j] = min(down, diagonal)
                front = cur
            return front[0]
    # ste 5: store the ans.
print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))

# time and space complexity
# -------------------------
# time --> O(n*n)
# space -> O(2n) [front and cur] array




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


