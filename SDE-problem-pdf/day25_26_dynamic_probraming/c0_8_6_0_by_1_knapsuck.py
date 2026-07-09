"""
--problem--
-----------
A thief is robbing a store and can carry a maximal weight of W into his knapsack. There are N items and the ith item weighs wi and is of value vi. Considering the constraints of the maximum weight that a knapsack can carry,
 you have to find and return the maximum value that a thief can generate by stealing items.

--example--
-----------
Input Format:
The first line contains a single integer T representing the number of test cases.      
The T-test cases are as follows:

Line 1:The first line contains an integer, that denotes the value of N. 
Line 2:The following line contains N space-separated integers, that denote the values of the weight of items. 
Line 3:The following line contains N space-separated integers, that denote the values associated with the items. 
Line 4:The following line contains an integer that denotes the value of W. W denotes the maximum weight that a thief can carry.
Output Format :
The first and only line of output contains the maximum value that a thief can generate, as described in the task. 
The output of every test case is printed in a separate line.


Time Limit: 1 second
Follow Up:
Can we solve this using space complexity of not more than O(W)?
Sample Input:
1 
4
1 2 4 5
5 4 8 6
5
Sample Output:
13



--Constraints--
---------------
Constraints:
1 <= T <= 10
1 <= N <= 10^2
1<= wi <= 50
1 <= vi <= 10^2
1 <= W <= 10^3


--link--
--------
https://www.codingninjas.com/codestudio/problems/0-1-knapsack_920542


complexity
-----------
MEDIUM

"""

# Recurssion
# ==========================
# step 1: represent the problem as index. -- do base case 1) destiation 2) out of bound check
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem


## Read input as specified in the question.
## Print output as specified in the question.

def knapsuck(n,weights,val,w):
    # base case
    return knapsuck_rec(n-1, weights, val, w)
def knapsuck_rec(i,weights,val,w):
    if i == 0 :
        if weights[i] <= w:
            return val[i]

        return 0
    
    not_pick = 0 + knapsuck_rec(i-1, weights,val,w)
    pick = 0
    if weights[i] <= w:
        pick = val[i] + knapsuck_rec(i-1, weights,val,w - weights[i])
    return max(pick,not_pick)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        weights = [int(x) for x in input().split(" ")]
        val = [int(x) for x in input().split(" ")]
        w = int(input())
        knapsuck(n,weights,val,w)

# time and space complexity
# -------------------------
# time --> 
# space ->


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================

    # step 2 :cheking the suproblem already solved or not.

    # step 3 : assign this sub problem ans to dp arrray.
# step 1 : define dp array.
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
    # careful about the index -- leave the base case index -- since that is already filled

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


