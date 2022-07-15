"""
--problem--
-----------
Given number of pages in n different books and m students. The books are arranged in ascending order of number of pages. Every student is assigned to read some consecutive books.
The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum. 

--example--
-----------
Input : pages[] = {12, 34, 67, 90} , m = 2
Output : 113
Explanation:
There are 2 number of students. Books can be distributed 
in following fashion : 
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student 
      '2' with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student
      '2' with 67 + 90 = 157 pages 
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student 
      '1' with 12 + 34 + 67 = 113 pages

Of the 3 cases, Option 3 has the minimum pages = 113. 

--link--
--------
https://www.geeksforgeeks.org/allocate-minimum-number-pages/


complexity
-----------
HARD

"""
import re


def allocate_books(books, students):
    res = 0
    low = max(books); high = sum(books)
    print("low, hihg", low,high)
    print("books",books)
    while high >= low:
        mid = (low + high) // 2
        print("mid", mid)
        if can_place_books(books, mid, students):
            print("can place moving high")
            res = mid
            high = mid - 1
        else:
            print("can't place moving low")
            low = mid + 1
        print("low,high",low, high)
    return res

def can_place_books(books, barrier, stu):
    allocated_stu = 1
    pages = 0
    for i in range(0, len(books)):
        if books[i] > barrier: return False
        if pages + books[i] > barrier:
            print("pages greter than barrer")
            allocated_stu +=1
            pages = 0
            pages += books[i]
            print("allocated stu, pages", allocated_stu, pages)
        else:
           
            pages += books[i]
            print("pages less tha barrier -- pages",pages)
    if allocated_stu > stu:
        return False
    if allocated_stu < stu:
        return False
    return True


a = allocate_books([12, 34, 67, 90], 2)
print(a) # 113








# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""
low, hihg 90 203
books [12, 34, 67, 90]
mid 146
pages less tha barrier -- pages 12
pages less tha barrier -- pages 46
pages less tha barrier -- pages 113
pages greter than barrer
allocated stu, pages 2 90
can place moving high
low,high 90 145
mid 117
pages less tha barrier -- pages 12
pages less tha barrier -- pages 46
pages less tha barrier -- pages 113
pages greter than barrer
allocated stu, pages 2 90
can place moving high
low,high 90 116
mid 103
pages less tha barrier -- pages 12
pages less tha barrier -- pages 46
pages greter than barrer
allocated stu, pages 2 67
pages greter than barrer
allocated stu, pages 3 90
can't place moving low
low,high 104 116
mid 110
pages less tha barrier -- pages 12
pages less tha barrier -- pages 46
pages greter than barrer
allocated stu, pages 2 67
pages greter than barrer
allocated stu, pages 3 90
can't place moving low
low,high 111 116
mid 113
pages less tha barrier -- pages 12
pages less tha barrier -- pages 46
pages less tha barrier -- pages 113
pages greter than barrer
allocated stu, pages 2 90
can place moving high
low,high 111 112
mid 111
pages less tha barrier -- pages 12
pages less tha barrier -- pages 46
pages greter than barrer
allocated stu, pages 2 67
pages greter than barrer
allocated stu, pages 3 90
can't place moving low
low,high 112 112
mid 112
pages less tha barrier -- pages 12
pages less tha barrier -- pages 46
pages greter than barrer
allocated stu, pages 2 67
pages greter than barrer
allocated stu, pages 3 90
can't place moving low
low,high 113 112
113
"""