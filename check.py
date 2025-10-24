class Solution:
    def median(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        median_index = (rows * cols) // 2 
        number_less_than_medin = median_index 

        def have_ele_median_less_than_mid(mid):
            # go over each row and do a bin-search and find how many elements < mid is there.
            count = 0
            for row in range(rows):
                l = 0
                h = cols - 1
                ans = h
                while l <= h:
                    m = (l+h)//2
                    if mat[row][m] < mid:
                        ans = m 
                        # we are looking for hte last true - got right and search more.
                        l = m + 1
                    else:
                        h = m - 1
                count += (ans + 1) # if the index is 2, than there is 3 elements in the row < k.

            return count 
        
        low = min(row[0] for row in mat)         # smallest element (first of each row)
        high = max(row[-1] for row in mat)
        ans = high

        while low<=high:
            mid = (low + high) // 2

            num_count = have_ele_median_less_than_mid(mid)
            if num_count == number_less_than_medin:
                return mid
            
            elif num_count > number_less_than_medin:
                high = mid - 1
            else:
                low = mid + 1
            

        return ans
    

Solution().median([[1, 3, 5], 
[2, 6, 9], 
[3, 6, 9]])