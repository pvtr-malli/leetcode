class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            dp.append([-1] * (n))
        return self.uniquePaths_rec(m-1, n-1,dp)
    def uniquePaths_rec(self, i,j,dp):
        if i==0 and j ==0:
            return 1
        if i<0 or j<0:
            return 0

        if dp[i][j] != -1:
            dp[i][j]
        up = self.uniquePaths_rec(i-1, j, dp)
        left = self.uniquePaths_rec(i, j-1, dp)
        return up + left



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m+1):
            dp.append([0] * (n+1))
        # base case
        dp[0][0] = 1
        # zero base case assignment is not needed -- since already zero
        for i in range(0,m):
            for j in range(0,n):
                if i ==0 and j ==0: dp[0][0] = 1
                else:
                    up=left=0
                    if i>0: up = dp[i-1][j] 
                    if j>0: left = dp[i][j-1]
                    dp[i][j]= up+left
        print(dp)
        return dp[m-1][n-1]

print(Solution().uniquePaths(3,7))