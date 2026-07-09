"""
--problem--
-----------
There is a new barn with N stalls and C cows. The stalls are located on a straight line at positions x1,….,xN (0 <= xi <= 1,000,000,000). We want to assign the cows to the stalls,
 such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

--example--
-----------
Examples:

Input: No of stalls = 5 
       Array: {1,2,8,4,9}
       And number of cows: 3

Output: One integer, the largest minimum distance 3

--link--
--------
https://takeuforward.org/data-structure/aggressive-cows-detailed-solution/


complexity
-----------
HARD

"""

def aggresive_cows(distance, cows):
    n = len(distance) 
    res = 0
    low = 1; high = distance[n - 1] - distance[0]
    while high >= low:
        mid = (low + high) // 2
        if can_place_cows(distance, mid, n, cows):
            res = mid
            low = mid + 1
        else:
            high = mid - 1

    return res

def can_place_cows(arr, dist, n, cows):
    last_placed_cow = arr[0]; count = 1
    for i in range(1, n):
        if arr[i] - last_placed_cow >= dist:
            last_placed_cow = arr[i]
            count += 1
        if count == cows:
            return True
    return False


a = aggresive_cows([1,2,4,8,9], 3)
print(a) # 3




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""