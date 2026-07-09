# Data Structure Time Complexity Cheat Sheet

## Array

| Operation        | Average | Worst |
|-----------------|---------|-------|
| Access (index)  | O(1)    | O(1)  |
| Search          | O(n)    | O(n)  |
| Insert (end)    | O(1)*   | O(n)  |
| Insert (middle) | O(n)    | O(n)  |
| Delete (end)    | O(1)    | O(1)  |
| Delete (middle) | O(n)    | O(n)  |

*amortized for dynamic array

---

## Stack

| Operation | Average | Worst |
|-----------|---------|-------|
| Push      | O(1)    | O(1)  |
| Pop       | O(1)    | O(1)  |
| Peek/Top  | O(1)    | O(1)  |
| Search    | O(n)    | O(n)  |

---

## Queue / Deque

| Operation      | Average | Worst |
|---------------|---------|-------|
| Enqueue       | O(1)    | O(1)  |
| Dequeue       | O(1)    | O(1)  |
| Peek (front)  | O(1)    | O(1)  |
| Search        | O(n)    | O(n)  |

---

## Singly Linked List

| Operation         | Average | Worst |
|------------------|---------|-------|
| Access (index)   | O(n)    | O(n)  |
| Search           | O(n)    | O(n)  |
| Insert (head)    | O(1)    | O(1)  |
| Insert (tail)    | O(n)    | O(n)  |
| Insert (middle)  | O(n)    | O(n)  |
| Delete (head)    | O(1)    | O(1)  |
| Delete (tail)    | O(n)    | O(n)  |
| Delete (middle)  | O(n)    | O(n)  |

---

## Doubly Linked List

| Operation         | Average | Worst |
|------------------|---------|-------|
| Access (index)   | O(n)    | O(n)  |
| Search           | O(n)    | O(n)  |
| Insert (head)    | O(1)    | O(1)  |
| Insert (tail)    | O(1)    | O(1)  |
| Insert (middle)  | O(n)    | O(n)  |
| Delete (head)    | O(1)    | O(1)  |
| Delete (tail)    | O(1)    | O(1)  |
| Delete (middle)  | O(n)    | O(n)  |

---

## Hash Map / Hash Set

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert    | O(1)    | O(n)  |
| Delete    | O(1)    | O(n)  |
| Search    | O(1)    | O(n)  |
| Access    | O(1)    | O(n)  |

*Worst case due to hash collisions*

---

## Binary Search Tree (BST)

| Operation | Average   | Worst |
|-----------|-----------|-------|
| Insert    | O(log n)  | O(n)  |
| Delete    | O(log n)  | O(n)  |
| Search    | O(log n)  | O(n)  |
| Access    | O(log n)  | O(n)  |

*Worst case when tree is unbalanced (skewed)*

---

## Balanced BST (AVL / Red-Black Tree)

| Operation | Average   | Worst    |
|-----------|-----------|----------|
| Insert    | O(log n)  | O(log n) |
| Delete    | O(log n)  | O(log n) |
| Search    | O(log n)  | O(log n) |
| Access    | O(log n)  | O(log n) |

---

## Heap (Min/Max)

| Operation      | Average   | Worst    |
|---------------|-----------|----------|
| Insert        | O(log n)  | O(log n) |
| Delete (top)  | O(log n)  | O(log n) |
| Peek (top)    | O(1)      | O(1)     |
| Heapify       | O(n)      | O(n)     |
| Search        | O(n)      | O(n)     |

---

## Trie

| Operation | Average  | Worst   |
|-----------|----------|---------|
| Insert    | O(m)     | O(m)    |
| Search    | O(m)     | O(m)    |
| Delete    | O(m)     | O(m)    |

*m = length of the key/word*

---

## Graph (Adjacency List)

| Operation         | Average        |
|------------------|----------------|
| Add vertex       | O(1)           |
| Add edge         | O(1)           |
| Remove vertex    | O(V + E)       |
| Remove edge      | O(E)           |
| BFS / DFS        | O(V + E)       |

*V = vertices, E = edges*

---

## Sorting Algorithms

| Algorithm      | Best       | Average    | Worst      | Space  |
|---------------|------------|------------|------------|--------|
| Bubble Sort   | O(n)       | O(n²)      | O(n²)      | O(1)   |
| Selection Sort| O(n²)      | O(n²)      | O(n²)      | O(1)   |
| Insertion Sort| O(n)       | O(n²)      | O(n²)      | O(1)   |
| Merge Sort    | O(n log n) | O(n log n) | O(n log n) | O(n)   |
| Quick Sort    | O(n log n) | O(n log n) | O(n²)      | O(log n)|
| Heap Sort     | O(n log n) | O(n log n) | O(n log n) | O(1)   |
| Tim Sort      | O(n)       | O(n log n) | O(n log n) | O(n)   |
| Counting Sort | O(n + k)   | O(n + k)   | O(n + k)   | O(k)   |
| Binary Search | O(1)       | O(log n)   | O(log n)   | O(1)   |

---

## Space Complexity

| Structure        | Space  |
|-----------------|--------|
| Array           | O(n)   |
| Stack / Queue   | O(n)   |
| Linked List     | O(n)   |
| Hash Map/Set    | O(n)   |
| BST             | O(n)   |
| Heap            | O(n)   |
| Trie            | O(n·m) |
| Graph (Adj List)| O(V+E) |
