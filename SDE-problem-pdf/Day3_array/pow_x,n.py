"""
--problem--
-----------
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

--example--
-----------
Input: x = 2.00000, n = 10
Output: 1024.00000

"""

class Solution:
    def myPow(self, x,n):
        ans = 1
        negative = False
        if n < 0 : n = -1 * n; negative = True
        while n!=0:
            
            if n %2 == 0:
                x = x * x
                n = n/2
            else:
                ans = ans * x
                n = n - 1
        if negative: return 1 / ans
        return ans

a = Solution().myPow(2.00000, 10)
print(a)