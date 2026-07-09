"""
--problem--
-----------
Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
Note: The flattened list will be printed using the bottom pointer instead of next pointer.

--example--
-----------
Input:
5 -> 10 -> 19 -> 28
|     |     |     | 
7     20    22   35
|           |     | 
8          50    40
|                 | 
30               45
Output:  5-> 7-> 8- > 10 -> 19-> 20->
22-> 28-> 30-> 35-> 40-> 45-> 50.
Explanation:
The resultant linked lists has every 
node in a single level.
(Note: | represents the bottom pointer.)




Input:
5 -> 10 -> 19 -> 28
|          |                
7          22   
|          |                 
8          50 
|                           
30              
Output: 5->7->8->10->19->22->28->30->50
Explanation:
The resultant linked lists has every
node in a single level.

(Note: | represents the bottom pointer.)

--link--
--------
https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1


complexity
-----------
MEDIUM

"""

#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def merge_two_sorted_list(l1 , l2):

    temp = Node(0)
    res = temp
    while l1 != None and l2!=None:
        if (l1.data == l2.data) or (l1.data < l2.data):
            temp.bottom = l1
            l1 = l1.bottom
            temp = temp.bottom
        else:
            temp.bottom = l2
            l2 = l2.bottom
            temp = temp.bottom
    if l1 != None: temp.bottom = l1
    else: temp.bottom = l2
    return res.bottom

def flatten(root):
    #Your code here







# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""