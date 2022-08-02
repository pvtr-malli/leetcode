"""
--problem--
-----------
Mr. X is a professional robber planning to rob houses along a street. Each house has a certain amount of money hidden. All houses along this street are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
You are given an array/list of non-negative integers 'ARR' representing the amount of money of each house. Your task is to return the maximum amount of money Mr. X can rob tonight without alerting the police.
Note:
It is possible for Mr. X to rob the same amount of money by looting two different sets of houses. Just print the maximum possible robbed amount, irrespective of sets of houses robbed.

--example--
-----------

For Example:
(i) Given the input array arr[] = {2, 3, 2} the output will be 3 because Mr X cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses. So, he’ll rob only house 2 (money = 3)

(ii) Given the input array arr[] = {1, 2, 3, 1} the output will be 4 because Mr X rob house 1 (money = 1) and then rob house 3 (money = 3).

(iii) Given the input array arr[] = {0} the output will be 0 because Mr. X has got nothing to rob.
Input Format :
The first line of input contains an integer 'T' representing the number of the test case. Then the test case follows.

The first line of each test case contains an integer, ‘N’ representing the size of the first array/list.

The second line of each test case contains 'N' single space-separated integers representing the array/list elements.
Output Format :
For each test case, print a single line containing a single integer denoting the maximum money that can be robbed in a separate line.

The output of each test case will be printed in a separate line.
Note:
You do not need to print anything; it has already been taken care of. Just implement the given function.
Constraints:
1 <= T <= 10
1 <= N <= 5 x 10 ^ 3
1 <= ARR[i] <= 10 ^ 9

Time limit: 1 sec.
Sample Input 1:
3
1
0
3
2 3 2
4
1 3 2 1
Sample Output 1:
0
3
4
Explanation Of Input 1:
(i) Mr. X has only one house to rob, but with no money.

(ii) Mr. X cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses (remember, it’s a circular street). So, he’ll rob only house 2 (money = 3) with a maximum value

(iii) Mr. X will get maximum value when he robs house 2 (money = 3) and then robs house 4 (money = 1) i.e. 4 units of money.
Sample Input 2:
3
5
1 5 1 2 6
3
2 3 5
4
1 3 2 0
Sample Output 2:
11
5
3

--Constraints--
---------------



--link--
--------

https://www.codingninjas.com/codestudio/problems/house-robber_839733
complexity
-----------
MEDIUM

"""

# Recurssion -- this will exceed the time limit -- do memoization
# ==========================
# step 1: represent the problem as index.
def houseRobber(valueInHouse):
    
    n = len(valueInHouse)
    if n == 1: return valueInHouse[0]
    without_first =  houseRobber_rec(valueInHouse[1:], n-2)
    without_last = houseRobber_rec(valueInHouse[:-1], n-2)
    return max(without_first, without_last)

def houseRobber_rec(nums, n):
    if n == 0:
        return nums[0]
    
    # step 2: Do all stuffs with the index
    pick = nums[n]
    # when we are at '1' index we can't move 2 steps -- so putting a check here.
    if n > 1:
        pick += houseRobber_rec(nums, n-2)
    not_pick = 0 + houseRobber_rec(nums, n-1)
    
    # step 3: return min/max/sum --according to the problem
    return max(pick,not_pick)



# time and space complexity
# -------------------------
# time --> 
# space ->


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================
def houseRobber(nums):
    n = len(nums)
    if n == 1: return nums[0]
    # step 1 : define dp array.
    dp = [-1] * (n)
    without_first = houseRobber_rec(nums[1:], n-2, dp)
    dp = [-1] * (n)
    without_last = houseRobber_rec(nums[:-1], n-2, dp)
    return max(without_first,without_last)

def houseRobber_rec(nums, n, dp):
    if n == 0:
        return nums[0]
    # step 2 :cheking the suproblem already solved or not.
    if dp[n] != -1:
        return dp[n]

    pick = nums[n]
    # when we are at '1' index we can't move 2 steps -- so putting a check here.
    if n > 1:
        pick += houseRobber_rec(nums, n-2,dp)
    not_pick = 0 + houseRobber_rec(nums, n-1, dp)
     # step 3 : assign this sub problem ans to dp arrray.
    dp[n] = max(pick,not_pick)
    return dp[n]
print(houseRobber([59, 53, 41, 26, 17, 13, 11]))
# assihn one extra space and left '0' index unused-- easy to call the index.

# time and space complexity
# -------------------------
# time --> 
# space ->


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.

        # step 4: Do what we need to do with the index.

    # ste 4: store the ans.

# time and space complexity
# -------------------------
# time --> 
# space ->


# Memory optimization (optimize space we have in tabulation)
# ==========================================================


# time and space complexity
# -------------------------
# time --> 
# space ->




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


