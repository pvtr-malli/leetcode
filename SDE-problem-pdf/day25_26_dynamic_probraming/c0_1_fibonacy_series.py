# Recurssion
import re


def fibonaci(n):
    if n <= 1:
        return n
    return fibonaci(n-1) + fibonaci(n-2)

print(fibonaci(4))

# MemoiZation(top - down) (getting dp array  in recurssion)
def fibonaci_memo(n,dp):
    if n <= 1:
        return n
    # step 2 :cheking the suproblem already solved or not.
    if dp[n] != -1:
        return dp[n]
    # step 3 : assign this sub problem ans to dp arrray.
    dp[n] = fibonaci_memo(n-1, dp) + fibonaci_memo(n-2, dp)
    # print(dp)
    return dp[n]
# step 1 : define dp array.
# assihn one extra space and left '0' index unused-- easy to call the index.
n = 4
dp_array = [-1] * (n+1) 
print(fibonaci_memo(n, dp_array))

# Tabulation(base/down - top) 
def fibonaci_tablu(n):
    # step 1: define the same dp size dp array.
    dp = [-1] * (n+1)

    # step 2: assign the values of base cases.
    dp[0] = 0
    dp[1] = 1
    # step 3: Find which index to which index we need to travers and do the for loop.
    for i in range(2,n+1):
        # step 4: Do what we need to do with the index.
        dp[i] = dp[i-1] + dp[i-2]
    # ste 4: store the ans.
    return dp[n]
print(fibonaci_tablu(4))
# Memory optimization (optimize space we have in tabulation)

def fibonaci_tablu_memory(n):

    # step 1: assign the values of base cases.
    prev2 = 0
    prev = 1
    # step 3: Find which index to which index we need to travers and do the for loop.
    for i in range(2,n+1):
        # step 4: Do what we need to do with the index.
        cur = prev+ prev2
        prev2 = prev
        prev = cur
    # ste 4: store the ans.
    return prev
print(fibonaci_tablu_memory(4))