"""
--problem--
-----------
Ninja is planing this ‘N’ days-long training schedule. Each day, he can perform any one of these three activities. (Running, Fighting Practice or Learning New Moves). Each activity has some merit points on each day. As Ninja has to improve all his skills, he can’t do the same activity in two consecutive days. Can you help Ninja find out the maximum merit points Ninja can earn?
You are given a 2D array of size N*3 ‘POINTS’ with the points corresponding to each day and activity. Your task is to calculate the maximum number of merit points that Ninja can earn.

--example--
-----------



--Constraints--
---------------



--link--
--------



complexity
-----------


"""

# Recurssion
# ==========================
# step 1: represent the problem as index.
def ninjaTraining(n, points) -> int:
    return ninjaTraining_rec(n-1, points, 3)

def ninjaTraining_rec(days, points, last_day):
    # step 2: Do all stuffs with the index
    if days == 0: 
        maxi = 0
        for i in range(3):
            if i != last_day:
                maxi = max(points[days][i], maxi)
        return maxi
    # for index out of pond error.
    if days < 0 :
        return 0
    # gonna try all the task which is not done in the previous day.
    maxi = 0
    for i in range(3):
        if i != last_day:
            point = points[days][i] + ninjaTraining_rec(days -1 , points, i)
            maxi = max(maxi, point)
    # step 3: return min/max/sum --according to the problem
    return maxi

print(ninjaTraining(3, [[1,2,5], [3 ,1 ,1] ,[3,3,3]]))


# time and space complexity
# -------------------------
# time --> 
# space ->


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================
def ninjaTraining_rec(days, points, last_day,dp):
    # step 2: Do all stuffs with the index
    if days == 0: 
        maxi = 0
        for i in range(3):
            if i != last_day:
                maxi = max(points[days][i], maxi)
        return maxi
    # for index out of pond error.
    if days < 0 :
        return 0
    # step 2 :cheking the suproblem already solved or not.
   
    if dp[days][last_day] != -1:
        return dp[days][last_day]
    # gonna try all the task which is not done in the previous day.
    maxi = 0
    for i in range(3):
        if i != last_day:
            point = points[days][i] + ninjaTraining_rec(days -1 , points, i, dp)
            maxi = max(maxi, point)
    # step 3 : assign this sub problem ans to dp arrray.
    dp[days][last_day] = maxi
    return dp[days][last_day]
    
# step 1 : define dp array.
def ninjaTraining(n, points) -> int:
    n = len(points)
    m = len(points[0])
    dp = []
    for row in range(len(points)):
        dp.append([-1]*(m+1))
    return ninjaTraining_rec(n-1, points, 3,dp)
print(ninjaTraining(3, [[1,2,5], [3 ,1 ,1] ,[3,3,3]]))
# assihn one extra space and left '0' index unused-- easy to call the index.

# time and space complexity
# -------------------------
# time --> 
# space ->


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.
def ninjaTraining(n, points) -> int:
    n = len(points)
    m = len(points[0])
    dp = []
    for row in range(len(points)):
        dp.append([-1]*(m+1))
    # step 2: assign the values of base cases.
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])
    # step 3: Find which index to which index we need to travers and do the for loop.
    for i in range(n):
        for j in range(m):
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


