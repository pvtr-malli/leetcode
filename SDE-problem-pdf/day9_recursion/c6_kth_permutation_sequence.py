"""
--problem--
-----------
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

--example--
-----------
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"

--link--
--------
https://leetcode.com/problems/permutation-sequence/


complexity
-----------
HARD

"""


class Solution:
    def getPermutation(self, n, k ):
        
        # step 1: find the factorial of (n-1)
        # find the number list
        fact = 1
        numbers = []
        for i in range(1,n):
            fact *= i
            numbers.append(i)
        numbers.append(n)

        # get k
        print("k,fact ",k,fact)
        k = k-1
        ans=""
        while True:
            # find the 
            ans = ans + str(numbers[k //fact])
            print("ans", ans,)
            # remove that element from numbers
            numbers.remove(numbers[k //fact])
            if len(numbers) == 0:
                break
            
            k = k % fact
            fact = fact // len(numbers)
            print("k,fact after one iteration",k,fact)
        return ans

a = Solution().getPermutation(4, 9)
print(a)




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""
k,fact  9 6
ans 2
k,fact after one iteration 2 2
ans 23
k,fact after one iteration 0 1
ans 231
k,fact after one iteration 0 1
ans 2314
2314
"""