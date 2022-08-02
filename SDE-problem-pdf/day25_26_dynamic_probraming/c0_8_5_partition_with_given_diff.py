"""
--problem--
-----------
Given an array ‘ARR’, partition it into two subsets (possibly empty) such that their union is the original array. Let the sum of the elements of these two subsets be ‘S1’ and ‘S2’.
Given a difference ‘D’, count the number of partitions in which ‘S1’ is greater than or equal to ‘S2’ and the difference between ‘S1’ and ‘S2’ is equal to ‘D’. Since the answer may be too large, return it modulo ‘10^9 + 7’.
If ‘Pi_Sj’ denotes the Subset ‘j’ for Partition ‘i’. Then, two partitions P1 and P2 are considered different if:
1) P1_S1 != P2_S1 i.e, at least one of the elements of P1_S1 is different from P2_S2.
2) P1_S1 == P2_S2, but the indices set represented by P1_S1 is not equal to the indices set of P2_S2. Here, the indices set of P1_S1 is formed by taking the indices of the elements from which the subset is formed.
Refer to the example below for clarification.
Note that the sum of the elements of an empty subset is 0.

--example--
-----------
For Example :
If N = 4, D = 3, ARR = {5, 2, 5, 1}
There are only two possible partitions of this array.
Partition 1: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
Partition 2: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
These two partitions are different because, in the 1st partition, S1 contains 5 from index 0, and in the 2nd partition, S1 contains 5 from index 2.
Input Format :
The first line contains a single integer ‘T’ denoting the number of test cases, then each test case follows:

The first line of each test case contains two space-separated integers, ‘N’ and ‘D,’ denoting the number of elements in the array and the desired difference.

The following line contains N integers denoting the space-separated integers ‘ARR’.
Output Format :
For each test case, find the number of partitions satisfying the above conditions modulo 10^9 + 7.
Output for each test case will be printed on a separate line.
Note :
You are not required to print anything; it has already been taken care of. Just implement the function.
Constraints :
1 ≤ T ≤ 10
1 ≤ N ≤ 50
0 ≤ D ≤ 2500
0 ≤ ARR[i] ≤ 50

Time limit: 1 sec
Sample Input 1 :
2
4 3
5 2 6 4
4 0
1 1 1 1
Sample Output 1 :
1
6
Explanation For Sample Input 1 :
For test case 1:
We will print 1 because :
There is only one possible partition of this array.
Partition : {6, 4}, {5, 2}. The subset difference between subset sum is: (6 + 4) - (5 + 2) = 3

For test case 2:
We will print 6 because :
The partition {1, 1}, {1, 1} is repeated 6 times:
Partition 1 : {ARR[0], ARR[1]}, {ARR[2], ARR[3]}
Partition 2 : {ARR[0], ARR[2]}, {ARR[1], ARR[3]}
Partition 3 : {ARR[0], ARR[3]}, {ARR[1], ARR[2]}
Partition 4 : {ARR[1], ARR[2]}, {ARR[0], ARR[3]}
Partition 5 : {ARR[1], ARR[3]}, {ARR[0], ARR[2]}
Partition 6 : {ARR[2], ARR[3]}, {ARR[0], ARR[1]}
The difference is in the indices chosen for the subset S1(or S2).
Sample Input 2 :
3
3 1
4 6 3
5 0
3 1 1 2 1
5 1
3 2 2 5 1
Sample Output 2 :
1
6
3



--Constraints--
---------------
1 ≤ T ≤ 10
1 ≤ N ≤ 50
0 ≤ D ≤ 2500
0 ≤ ARR[i] ≤ 50

Time limit: 1 sec


--link--
--------
https://www.codingninjas.com/codestudio/problems/partitions-with-given-difference_3751628


complexity
-----------
MEDIUM

"""
# Recurssion
# ==========================
# step 1: represent the problem as index.
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem

import math


def countPartitions(n, d, arr) -> int:
    total_sum = sum(arr)
    # print(total_sum)
    if total_sum - d < 0:
        return 0
    if (total_sum - d ) % 2 == 1 : return 0
    return findWays_rec(n-1, (total_sum - d) // 2, arr)

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

print(countPartitions(4, 3, [5,2,6,4]))


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

def countPartitions(n, d, arr) -> int:
    total_sum = sum(arr)
    # print(total_sum)
    if total_sum - d < 0:
        return 0
    if (total_sum - d ) % 2 == 1 : return 0
    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    # step 1:
    tar = (total_sum - d )//2
    dp = []
    for i in range(n):
        dp.append([-1]*(tar+1))
    # print(dp)
    return findWays_rec(n-1, tar,arr, dp)

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
def countPartitions(n, d, arr) -> int:
    mod = int(math.pow(10,9) + 7)
    print(mod)
    total_sum = sum(arr)
    # print(total_sum)
    if total_sum - d < 0:
        return 0
    if (total_sum - d ) % 2 != 0 : return 0
    target = (total_sum - d )//2
    # step 1:
    dp = []
    for i in range(n):
        dp.append([0]*(target+1))
    # step 2:
    if arr[0] == 0:
        dp[0][0] = 2
    else:
        dp[0][0] = 1
    # for i in range(n):
    #     dp[i][0] = 1
    if arr[0] != 0 and arr[0] <=target:
        dp[0][arr[0]] = 1
    # step 3:
    for i in range(1,n):
        for tar in range(0,target+1):

            # step 4
            not_take = dp[i-1][tar]
            take = 0
            if arr[i] <= tar:
                take = dp[i-1][tar-arr[i]]
            dp[i][tar] = (take + not_take) % mod # asked in the question if the ans too long mod it with 10**9+7
            # print(take + not_take)
            # print(dp)
    return dp[n-1][target] 
print(countPartitions(6,17, [1,0,8,5,1,4]))

# time and space complexity
# -------------------------
# time --> O(n*target)
# space -> O(n*target)


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
def countPartitions(n, d, arr) -> int:
    mod = int(math.pow(10,9) + 7)
    total_sum = sum(arr)
    # print(total_sum)
    if total_sum - d < 0:
        return 0
    if (total_sum - d ) % 2 != 0 : return 0
    target = (total_sum - d )//2
    # step 1:
    prev = [0] *(target+1)
    if arr[0] == 0:
        prev[0] = 2
    else:
        prev[0] = 1
    # for i in range(n):
    #     dp[i][0] = 1
    if arr[0] != 0 and arr[0] <=target:
        prev[arr[0]] = 1
    # step 3:
    for i in range(1,n):
        cur = [0] * (target+1)
        if arr[0] == 0:
            cur[0] = 2
        else:
            cur[0] = 1
        for tar in range(0,target+1):

            # step 4
            not_take = prev[tar]
            take = 0
            if arr[i] <= tar:
                take = prev[tar-arr[i]]
            cur[tar] = (take + not_take) % mod
            # print(take + not_take)
            # print(dp)
        prev = cur
    return prev[tar] 
#print(subsetSumToK(4,100, [4,3,2,1]))


# output
"""

"""


