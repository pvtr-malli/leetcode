
def binary_search(nums, target):

    # edge case.
    if len(nums) == 1:
        return (0 if nums[0] == target else -1)

    low = 0; high =len(nums)-1
    print("array, target", nums, target)
    while high >= low:
        mid = (high+low) // 2

        if nums[mid] == target: return mid

        if mid < target:
            # serach right side.
            low = mid + 1
        else:
            # search left side.
            high = mid - 1
        
    return -1 # target not present in the list.


a= binary_search([0,1,2,4,5,6,7], 3)
print(a) # -1

a= binary_search([0,1,2,3,4,5,6,7], 5)
print(a) 

a= binary_search([0,1,2,3,4,5,6,7], 7)
print(a)

a= binary_search([0,1,2,3,4,5,6,7], 0)
print(a)



"""
array, target [0, 1, 2, 4, 5, 6, 7] 3
-1
array, target [0, 1, 2, 3, 4, 5, 6, 7] 5
5
array, target [0, 1, 2, 3, 4, 5, 6, 7] 7
7
array, target [0, 1, 2, 3, 4, 5, 6, 7] 0
0

"""