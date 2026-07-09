# The problems:

# 1 _ array:
- Subarray – a continuous part of the array.
    - Ex: Array = [1,2,3,4,5]
    - Subarrays: [1,2,3], [2,3,4,5], [4]
- Subsequence – elements taken in order, not necessarily contiguous.
    - Ex: Array = [1,2,3,4,5]
    - Subsequences: [1,3,5], [2,4], [1,2,3,4,5]
- Subset – any combination of elements, order doesn’t matter.
    - Ex: Array = [1,2,3]
    - Subsets: [], [1], [2,3], [1,2,3]

## 2 _ Grid
- Always spoling the out of index thingy in grid related sums. be very careful. write it down not an issue.
    - Qiick and need solution, have a space aorund the matrix, create dp for n+2 so you can just do the thing
      no need to worry about the out of index error.


## 3_subsets
- The dp, need not to be a array. you just need a DS to track the already visited values.
    - it can be dict too, if you are having more than 2 variables to track, see -- 3_474._ones_and_zeroes_medium.ipynb
```
d = {}
d[(1, (1,2))] = 1  # has like this, list can't be a key so keep it as a tuple.
```
- 4_322._coin_change_medium.ipynb: see how I did the **tabulation** there. and the base case. where I havr to return -1 when it's not possible. understand how I am returning the -1 in this case.


subset sum quals k(0/1 knapsoack) == coin change (unbounded knapsoack)

- subset vs subarray difference INPORTANT see :0_560._subarray_sum_equals_k_medium.ipynb

## 6_ dtrings
- start the recurssion from the back. So the tabulaiton we can do the for loop for 1 - > n+1
- s[0 to i-1] means in my world, when i = 3. we will consider 0 to (3-1) indexes. which is 0,1 and 2.




# Common:
- In tabulation: The last ans returning thing is:
- return dp[0][n-1] # NOTE: this is the numbers you call the plain recursion with.