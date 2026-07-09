"""
--problem--
-----------
You are given an array (0-based indexing) of positive integers and you have to tell how many different ways of selecting the elements from the array are there 
such that the sum of chosen elements is equal to the target number “tar”.
Note:
Two ways are considered different if sets of indexes of elements chosen by these ways are different.

Input is given such that the answer will fit in a 32-bit integer.

--example--
-----------
For Example:
If N = 4 and tar = 3 and the array elements are [1, 2, 2, 3], then the number of possible ways are:
{1, 2}
{3}
{1, 2}
Hence the output will be 3.
Input Format :
The first line of the input contains an integer, 'T’, denoting the number of test cases.

The first line of each test case will contain two space-separated integers ‘N’ and “tar”, denoting the size of the array and the target sum.

The second line of each test case contains ‘N’ space-separated integers denoting elements of the array.
Output Format :
For each test case, print the number of ways that satisfy the condition mentioned in the problem statement.

Print a separate line for each test case.
Note :
You do not need to print anything, it has already been taken care of. Just implement the given function.
Constraints:
1 <= T <= 10
1 <= N <= 100
0 <= nums[i] <= 1000
1 <= tar <= 1000

Time limit: 1 sec
Sample Input 1 :
2
4 3
1 2 2 3
2 3
1 2
Sample Output 1 :
 3
 1
Explanation For Sample Output 1:
For the first test case, N = 4 and tar = 3 and array elements are [1, 2, 2, 2,3] then the number of possible ways of making sum = 5 are:
{1,2}
{3}
{1,2}

Hence the output will be 3.

For the second test case, N = 2 and tar = 3 and array elements are [1, 2], there is only one way of making sum = 3 which is {1,2}.

Hence the output will be 1.
Sample Input 2 :
2
3 4
12 1 3
2 41
2 34
Sample Output 2 :
1
0


--Constraints--
---------------
1 <= T <= 10
1 <= N <= 100
0 <= nums[i] <= 1000
1 <= tar <= 1000

Time limit: 1 sec


--link--
--------
https://www.codingninjas.com/codestudio/problems/number-of-subsets_3952532


complexity
-----------
MEDIUM

"""

# Recurssion
# ==========================
# step 1: represent the problem as index.
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem
def findWays(num, tar) -> int:
    n = len(num)
    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    return findWays_rec(n-1, tar,num)

def findWays_rec(i, k, arr):
    #print(i,k)
    if i == 0:
        if arr[0] == 0 and k == 0 : return 2
        if k == 0: return 1
        if arr[0] == k: return 1
        return 0
    take = 0
    if arr[i] <= k:
        take = findWays_rec(i-1, k-arr[i], arr)
    not_take = findWays_rec(i-1, k , arr)
    return take + not_take

print(findWays([12,1,3], 4))


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

def findWays(num, tar) -> int:
    n = len(num)
    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    # step 1:
    dp = []
    for i in range(n):
        dp.append([-1]*(tar+1))
    # print(dp)
    return findWays_rec(n-1, tar,num, dp)

def findWays_rec(i, k, arr, dp):
    if i == 0:
        if arr[0] == 0 and k == 0 : return 2
        if k == 0: return 1
        if arr[0] == k: return 1
        return 0
    # step 3:
    if dp[i][k] != -1:
        return dp[i][k]
    take = False
    if arr[i] <= k:
        take = findWays_rec(i-1, k-arr[i], arr, dp)
    not_take = findWays_rec(i-1, k , arr, dp)
    # step2:
    dp[i][k] =  take + not_take
    return dp[i][k]
#rint(subsetSumToK(4,5, [4,3,2,1]))
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
def findWays(arr, tar) -> int:
    n = len(arr)

    # step 1:
    dp = []
    for i in range(n):
        dp.append([0]*(tar+1))
    # step 2:
    dp[0][0] = 2
    for i in range(n):
        dp[i][0] = 1
    if arr[0] <=tar:
        dp[0][arr[0]] = 1
    # step 3:
    for i in range(1,n):
        for tar in range(0,tar+1):

            # step 4
            not_take = dp[i-1][tar]
            take = 0
            if arr[i] <= tar:
                take = dp[i-1][tar-arr[i]]
            dp[i][tar] = take + not_take
            # print(take + not_take)
            # print(dp)
    return dp[n-1][tar] 
#print(subsetSumToK(3,4, [2,3,1]))

# time and space complexity
# -------------------------
# time --> O(n*target)
# space -> O(n*target)


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
def findWays(arr, tar) -> int:
    n = len(arr)
    # step 1:
    prev = [0] * (tar+1)
    # step 2:
    prev[0] = 2
    
    prev[0] = 1
    if arr[0] <=tar:
        prev[arr[0]] = 1
    # step 3:
    for i in range(1,n):
        cur = [0] * (tar+1)
        cur[0] = 1
        for tar in range(0,tar+1):

            # step 4
            not_take = prev[tar]
            take = 0
            if arr[i] <= tar:
                take = prev[tar-arr[i]]
            cur[tar] = take + not_take
            # print(take + not_take)
            # print(dp)
        prev = cur
    return prev[tar] 
#print(subsetSumToK(4,100, [4,3,2,1]))



# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


