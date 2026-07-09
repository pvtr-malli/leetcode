"""
--problem--
-----------
Problem Statement
You have been given an N*M matrix filled with integer numbers, find the maximum sum that can be obtained from a path starting from any cell in the first row to any cell in the last row.
From a cell in a row, you can move to another cell directly below that row, or diagonally below left or right. So from a particular cell (row, col), we can move in three directions i.e.
Down: (row+1,col)
Down left diagonal: (row+1,col-1)
Down right diagonal: (row+1, col+1)

--example--
-----------
Input Format :
The first line contains an integer 'T', which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case contains two Integers 'N' and 'M' where 'N' denotes the number of rows in the given matrix. And 'M' denotes the number of columns in the given matrix.

The next 'N' line of each test case contains 'M' space-separated integers denoting the cell elements.
Output Format :
For each test case/query, print the maximum sum that can be obtained by taking a path as described above.

Output for every test case will be printed in a separate line.
Note :
You do not need to print anything. It has already been taken care of.




Input 1 :
2
4 4
1 2 10 4
100 3 2 1
1 1 20 2
1 2 2 1
3 3
10 2 3
3 7 2
8 1 5
Output 1 :
105
25
Explanation Of Input 1 :
In the first test case for the given matrix,

The maximum path sum will be 2->100->1->2, So the sum is 105(2+100+1+2).

In the second test case for the given matrix, the maximum path sum will be 10->7->8, So the sum is 25(10+7+8).
Input 2 :
2
3 3
1 2 3
9 8 7
4 5 6
4 6
10 10 2 -13 20 4
1 -9 -81 30 2 5
0 10 4 -79 2 -10
1 -5 2 20 -11 4
Output 2 :
17
74
Explanation Of Input 2 :
In the first test case for the given matrix, the maximum path sum will be 3->8->6, So the sum is 17(3+8+6).

In the second test case for the given matrix, the maximum path sum will be 20->30->4->20, So the sum is 74(20+30+4+20).



--Constraints--
---------------

1 <= T <= 50
1 <= N <= 100
1 <= M <= 100
-10^4 <= matrix[i][j] <= 10^4

Where 'T' is the number of test cases.
Where 'N' is the number of rows in the given matrix, and 'M' is the number of columns in the given matrix.
And, matrix[i][j] denotes the value at (i,j) cell in the matrix.

Time Limit: 1sec

--link--
--------
https://www.codingninjas.com/codestudio/problems/maximum-path-sum-in-the-matrix_797998


complexity
-----------
MEDIUM

"""

# Recurssion
# ==========================
# step 1: represent the problem as index. and base -- 1) destination base case 2) out of bound check base case
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem
from traceback import print_tb


def getMaxPathSum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    maxi = -1e9
    for j in range(m):
        m = getMaxPathSum_rec(n-1, j, matrix)
        maxi = max(m, maxi)
    return maxi

def getMaxPathSum_rec(i,j,matrix):
    #print(i,j)
    m = len(matrix[0])
    # outof bound index
    if j<0 or j>m-1:
        return -1e9
    
    if i ==0 : return matrix[i][j]
     # returning the min number
    
    up = matrix[i][j] + getMaxPathSum_rec(i-1, j, matrix)
    right_diagonal = matrix[i][j] + getMaxPathSum_rec(i-1, j+1, matrix)
    left_diagonal = matrix[i][j] + getMaxPathSum_rec(i-1, j-1, matrix)
    return max(up, right_diagonal, left_diagonal)


print(getMaxPathSum([[1,2,3], [9,8,7],[4,5,6]]))
# time and space complexity
# -------------------------
# time --> O(3**n) * m (for m cols) -- (exploring 3 paths for each element)
# space -> O(n)


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================

    # step 2 :cheking the suproblem already solved or not.

    # step 3 : assign this sub problem ans to dp arrray.
# step 1 : define dp array.
# assihn one extra space and left '0' index unused-- easy to call the index.


def getMaxPathSum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    maxi = -1e9
    dp = []
    for row in range(n):
        dp.append([-1]*(m))
    for j in range(m):
        m = getMaxPathSum_rec(n-1, j, matrix,dp)
        maxi = max(m, maxi)
    return maxi

def getMaxPathSum_rec(i,j,matrix,dp):
    m = len(matrix[0])
    # outof bound index
    if j<0 or j>m-1:
        return -1e9
    
    if i ==0 : return matrix[i][j]
     # returning the min number
    # step 2
    if dp[i][j] != -1 :
        return dp[i][j]
    up = matrix[i][j] + getMaxPathSum_rec(i-1, j, matrix, dp)
    right_diagonal = matrix[i][j] + getMaxPathSum_rec(i-1, j+1, matrix, dp)
    left_diagonal = matrix[i][j] + getMaxPathSum_rec(i-1, j-1, matrix, dp)
    # step 3
    dp[i][j] = max(up, right_diagonal, left_diagonal)
    return dp[i][j]

print(getMaxPathSum([[1,2,10,4], [100,3,2,1], [1,1,20,2],[1,2,2,1]]))
# time and space complexity
# -------------------------
# time --> O(n*m)
# space -> O(n*m)[dp] + O(n)[axilory]


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index. and check the out of boundary check

    # ste 4: store the ans.
def getMaxPathSum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    maxi = -1e9
    dp = []
    # step 1
    for row in range(n):
        dp.append([-1]*(m))
    # step 2
    for i in range(0,m):
        dp[0][i] = matrix[0][i]
    for i in range(1,n):
        for j in range(0,m):
            # boundary check + do stfuss
            up = matrix[i][j] + dp[i-1][j]
            right_diagonal = matrix[i][j]
            if j+1 < m:
                right_diagonal += dp[i-1][j+1]
            left_diagonal = matrix[i][j]
            if j > 0 :
                left_diagonal += dp[i-1][j-1]
            dp[i][j] = max(up,right_diagonal,left_diagonal)
    

    # this will run 0,0 - (n-1,m-1)
    # so all the values stored in the last line -- returning the max of last line is fine.
    for j in range(m):
        maxi = max(maxi, dp[n-1][j])
    return maxi
print(getMaxPathSum([[1,2,10,4], [100,3,2,1], [1,1,20,2],[1,2,2,1]]))
# time and space complexity
# -------------------------
# time --> O(n*m)
# space -> O(n*m)


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
def getMaxPathSum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    maxi = -1e9
    prev = [-1]*m
    # step 2
    for i in range(0,m):
        prev[i] = matrix[0][i]
    for i in range(1,n):
        cur = [-1] * m
        for j in range(0,m):
            # boundary check + do stfuss
            up = matrix[i][j] + prev[j]
            right_diagonal = matrix[i][j]
            if j+1 < m:
                right_diagonal += prev[j+1]
            left_diagonal = matrix[i][j]
            if j > 0 :
                left_diagonal += prev[j-1]
            cur[j] = max(up,right_diagonal,left_diagonal)
        prev = cur
    # this will run 0,0 - (n-1,m-1)
    # so all the values stored in the last line -- returning the max of last line is fine.
    for j in range(m):
        maxi = max(maxi, prev[j])
    return maxi
print(getMaxPathSum([[1,2,10,4], [100,3,2,1], [1,1,20,2],[1,2,2,1]]))
# time and space complexity
# -------------------------
# time --> O(n*m)
# space -> O(2n)[front and cur]




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


