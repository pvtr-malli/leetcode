"""
--problem--
-----------


--example--
-----------



"""
class Solution():
    def majority_path(self, a):
        count,i = 0,0
        while i< len(a):
            if count == 0:
                majority_ele = a[i]
                count +=1
            elif a[i] == majority_ele:
                count += 1
                
            else:
                count -= 1
            i += 1
            # print("majority_element", majority_ele)
            # print("count",count)
            # print("i",i)
        return majority_ele

a = Solution().majority_path([7,7,5,5,5,4,5,5]) 
print(a)
