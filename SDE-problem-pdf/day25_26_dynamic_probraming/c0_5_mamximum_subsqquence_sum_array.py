"""
--problem--
-----------
You are given an array/list of ‘N’ integers. You are supposed to return the maximum sum of the subsequence with the constraint that no two elements are adjacent in the given array/list.
Note:
A subsequence of an array/list is obtained by deleting some number of elements (can be zero) from the array/list, leaving the remaining elements in their original order.

--example--
-----------
Input Format:
The first line contains a single integer ‘T’ denoting the number of test cases.

The first line of each test case contains a single integer ‘N’ denoting the number of elements in the array.

The second line contains ‘N’ single space-separated integers denoting the elements of the array/list.
Output Format:
For each test case, print a single integer that denotes the maximum sum of the non-adjacent elements.

Print the output of each test case in a separate line.
Note:
You do not need to print anything; it has already been taken care of. Just implement the given function.


Sample Input 1:
2
3
1 2 4
4
2 1 4 9
Sample Output 1:
5
11
Explanation To Sample Output 1:
In test case 1, the sum of 'ARR[0]' & 'ARR[2]' is 5 which is greater than 'ARR[1]' which is 2 so the answer is 5.

In test case 2, the sum of 'ARR[0]' and 'ARR[2]' is 6, the sum of 'ARR[1]' and 'ARR[3]' is 10, and the sum of 'ARR[0]' and 'ARR[3]' is 11. So if we take the sum of 'ARR[0]' and 'ARR[3]', it will give the maximum sum of sequence in which no elements are adjacent in the given array/list.
Sample Input 2:
2
5
1 2 3 5 4
9
1 2 3 1 3 5 8 1 9
Sample Output 2:
8
24
Explanation To Sample Output 2:
In test case 1, out of all the possibilities, if we take the sum of 'ARR[0]', 'ARR[2]' and 'ARR[4]', i.e. 8, it will give the maximum sum of sequence in which no elements are adjacent in the given array/list.

In test case 2, out of all the possibilities, if we take the sum of 'ARR[0]', 'ARR[2]', 'ARR[4]', 'ARR[6]' and 'ARR[8]', i.e. 24 so, it will give the maximum sum of sequence in which no elements are adjacent in the given array/list.
--Constraints--
---------------
1 <= T <= 500
1 <= N <= 1000
0 <= ARR[i] <= 10^5

Where 'ARR[i]' denotes the 'i-th' element in the array/list.

Time Limit: 1 sec.


--link--
--------
https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261


complexity
-----------
MEDIUM

"""

# Recurssion
# ==========================
# step 1: represent the problem as index.
def maximumNonAdjacentSum(nums):
    n = len(nums)
    return maximumNonAdjacentSum_rec(nums, n-1)

def maximumNonAdjacentSum_rec(nums, n):
    if n == 0:
        return nums[0]
    
    # step 2: Do all stuffs with the index
    pick = nums[n]
    # when we are at '1' index we can't move 2 steps -- so putting a check here.
    if n > 1:
        pick += maximumNonAdjacentSum_rec(nums, n-2)
    not_pick = 0 + maximumNonAdjacentSum_rec(nums, n-1)
    
    # step 3: return min/max/sum --according to the problem
    return max(pick,not_pick)

print(maximumNonAdjacentSum([8,8]))
# time and space complexity
# -------------------------
# time --> O(2**n)
# space -> O(n)


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================
def maximumNonAdjacentSum(nums):
    n = len(nums)
    # step 1 : define dp array.
    dp = [-1] * (n+1)
    return maximumNonAdjacentSum_rec(nums, n-1, dp)

def maximumNonAdjacentSum_rec(nums, n, dp):
    if n == 0:
        return nums[0]
    # step 2 :cheking the suproblem already solved or not.
    if dp[n] != -1:
        return dp[n]

    pick = nums[n]
    # when we are at '1' index we can't move 2 steps -- so putting a check here.
    if n > 1:
        pick += maximumNonAdjacentSum_rec(nums, n-2,dp)
    not_pick = 0 + maximumNonAdjacentSum_rec(nums, n-1, dp)
     # step 3 : assign this sub problem ans to dp arrray.
    dp[n] = max(pick,not_pick)
    return dp[n]

# assihn one extra space and left '0' index unused-- easy to call the index.

# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)[dp] + O(n) [axilory]


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.
def maximumNonAdjacentSum(nums):
    n = len(nums)
    # step 1 : define dp array.
    dp = [-1] * (n+1)
    # step 2: assign the values of base cases.
    dp[0] = nums[0]
    # step 3: Find which index to which index we need to travers and do the for loop.
    for i in range(1, n):
        # step 4: Do what we need to do with the index.
        # step 2 :cheking the suproblem already solved or not.
        if dp[i] != -1:
            return dp[i]
        pick = nums[i]
        # when we are at '1' index we can't move 2 steps -- so putting a check here.
        if i > 1:
            pick += dp[i-2]
        not_pick = 0 + dp[i-1]
        dp[i] = max(pick, not_pick)
    # ste 4: store the ans.
    return dp[n-1]
# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)[dp]


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
def maximumNonAdjacentSum(nums):
    n = len(nums)

    # step 2: assign the values of base cases.
    prev = nums[0]
    prev2 = -1
    # step 3: Find which index to which index we need to travers and do the for loop.
    for i in range(1, n):
        # step 4: Do what we need to do with the index.
        pick = nums[i]
        # when we are at '1' index we can't move 2 steps -- so putting a check here.
        if i > 1:
            pick += prev2
        not_pick = 0 + prev
        cur = max(pick, not_pick)

        # update the values
        prev2 = prev
        prev = cur
    # ste 4: store the ans.
    return prev

# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(1)




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


