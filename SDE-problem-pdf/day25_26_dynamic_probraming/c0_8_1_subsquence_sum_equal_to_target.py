"""
--problem--
-----------
You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.
Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

--example--
-----------

For Example :
If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.
Input Format :
The first line contains a single integer T representing the number of test cases.

The first line of each test case contains two space-separated integers ‘N’ and ‘K’ representing the size of the input ‘ARR’ and the required sum as discussed above.

The next line of each test case contains ‘N’ single space-separated integers that represent the elements of the ‘ARR’.
Output Format :
For each test case, return true or false as discussed above.
Output for each test case will be printed in a separate line.
Note:
You don’t need to print anything, it has already been taken care of. Just implement the given function.


Time Limit: 1 sec
Sample Input 1:
2
4 5
4 3 2 1
5 4
2 5 1 6 7
Sample Output 1:
true
false
Explanation For Sample Input 1:
In example 1, ‘ARR’ is {4,3,2,1} and ‘K’ = 5. There exist 2 subsets with sum = 5. These are {4,1} and {3,2}. Hence, return true.
In example 2, ‘ARR’ is {2,5,1,6,7} and ‘K’ = 4. There are no subsets with sum = 4. Hence, return false.
Sample Input 2:
2
4 4
6 1 2 1
5 6
1 7 2 9 10
Sample Output 2:
true
false
Explanation For Sample Input 2:
In example 1, ‘ARR’ is {6,1,2,1} and ‘K’ = 4. There exist 1 subset with sum = 4. That is {1,2,1}. Hence, return true.
In example 2, ‘ARR’ is {1,7,2,9,10} and ‘K’ = 6. There are no subsets with sum = 6. Hence, return false.

--Constraints--
---------------

Constraints:
1 <= T <= 5
1 <= N <= 10^3
0 <= ARR[i] <= 10^9
0 <= K <= 10^3

--link--
--------
https://www.codingninjas.com/codestudio/problems/subset-sum-equal-to-k_1550954


complexity
-----------
MEDIUm

"""

# Recurssion
# ==========================
# step 1: represent the problem as index.
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem
def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    return subsetSumToK_rec(n-1, k,arr)

def subsetSumToK_rec(i, k, arr):
    if k == 0:
        return True
    if i ==0:
        return arr[0] == k
    take = False
    if arr[i] <= k:
        take = subsetSumToK_rec(i-1, k-arr[i], arr)
    not_take = subsetSumToK_rec(i-1, k , arr)
    return take or not_take

print(subsetSumToK(4,5, [4,3,2,1]))


# time and space complexity
# -------------------------
# time --> O(2**n)[for each arra index we have two path(take or not take)]
# space -> O(n)[axilory]


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================

    # step 2 :cheking the suproblem already solved or not.

    # step 3 : assign this sub problem ans to dp arrray.
# step 1 : define dp array.that shuld have all the variable things in the function call.
# assihn one extra space and left '0' index unused-- easy to call the index.
def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    # step 1:
    dp = []
    for i in range(n):
        dp.append([-1]*(k+1))
    # print(dp)
    return subsetSumToK_rec(n-1, k,arr, dp)

def subsetSumToK_rec(i, k, arr, dp):
    if k == 0:
        return True
    if i ==0:
        return arr[0] == k
    # step 3:
    if dp[i][k] != -1:
        return dp[i][k]
    take = False
    if arr[i] <= k:
        take = subsetSumToK_rec(i-1, k-arr[i], arr, dp)
    not_take = subsetSumToK_rec(i-1, k , arr, dp)
    # step2:
    dp[i][k] =  take or not_take
    return dp[i][k]
print(subsetSumToK(4,5, [4,3,2,1]))
# time and space complexity
# -------------------------
# time --> O(n*target) # we have n*target ==> states
# space -> O(n*target)[dp] + O(n)[axilory]


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index.

    # ste 4: store the ans.
def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    # step 1:
    dp = []
    for i in range(n):
        dp.append([False]*(k+1))
    # step 2:
    for i in range(n):
        dp[i][0] = True
    if arr[0]<=k:
        dp[0][arr[0]] = True
    # step 3:
    for i in range(1,n):
        for tar in range(1,k+1):
            print(i,tar)
            # step 4
            not_take = dp[i-1][tar]
            take = False
            if arr[i] <= tar:
                take = dp[i-1][tar-arr[i]]
            dp[i][tar] = take or not_take
            print(take or not_take)
            print(dp)
    return dp[n-1][k] 
print(subsetSumToK(3,4, [2,3,1]))

# time and space complexity
# -------------------------
# time --> O(n*target)
# space -> O(n*target)


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    # step 1:
    prev = [False] * (k+1)
    
    # step 2:
    prev[0] = True
    if arr[0]<=k:
        prev[arr[0]] = True
    # step 3:
    for i in range(1,n):
        cur = [False] * (k+1)
        cur[0] = True
        for tar in range(1,k+1):
            # step 4
            not_take = prev[tar]
            take = False
            if arr[i] <= tar:
                take = prev[tar-arr[i]]
            cur[tar] = take or not_take
        prev = cur
    return prev[k] 
print(subsetSumToK(4,100, [4,3,2,1]))

# time and space complexity
# -------------------------
# time --> O(n*target)
# space -> O(1)




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


