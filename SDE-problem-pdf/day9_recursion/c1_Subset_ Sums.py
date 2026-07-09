"""
--problem--
-----------
Given a list arr of N integers, print sums of all subsets in it.

--example--
-----------
Input:
N = 2
arr[] = {2, 3}
Output:
0 2 3 5
Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then 
Sum = 2+3 = 5.

--link--
--------
https://practice.geeksforgeeks.org/problems/subset-sums2234/1


complexity
-----------
BAISC

"""

#User function Template for python3

def subsetSums(arr, i, length, sum_of_subset, result):
        if i == length:
            result.append(sum_of_subset)
            return
        # pick the current element
        subsetSums(arr, i+1, length, sum_of_subset + arr[i], result)

        # Not pick the current element
        subsetSums(arr, i+1, length, sum_of_subset, result)


arr = [2,3]
res = []
subsetSums(arr, 0, len(arr) , sum_of_subset=0, result=res)
print("subset sum ",res)


# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""