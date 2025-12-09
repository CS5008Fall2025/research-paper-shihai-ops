[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zBqi0PeJ)
# Research Paper
* Name: Haisheng Shi
* Semester: Fall 2025
* Topic: AVL Tree and its comparison with BST Tree. 



Note the following is an example outline to help you. Please rework as you need, you do not need to follow the section heads and *YOU SHOULD NOT* make everything a bulleted list. This needs to read as an executive report/research paper. 

## Introduction
- What is the algorithm/datastructure?
- What is the problem it solves? 
- Provide a brief history of the algorithm/datastructure. (make sure to cite sources)
- Provide an introduction to the rest of the paper. 
This study focuses on the properties of the AVL Tree and its implementation. The AVL tree is one of the most important data structures invented by Georgy Adelson-Velsky and Evgenii Landis	in 1962. It creatively resolved the problem of BST(Binary Search Tree) when processing well-sorted data. In this case, the BST will degrade to a linked list and the time complexity of search, insert and delete would be $O(n)$. To solve this problem, the AVL tree introduces a self-balancing property where the heights of the two child subtrees of any node differ by at most one (known as the Balance Factor). If this property is violated during an insertion or deletion, the tree automatically restores balance through a series of rotation operations (Left, Right, Left-Right, or Right-Left). This mechanism guarantees that the tree height always remains logarithmic relative to the number of nodes, ensuring a time complexity of $O(\log n)$ for search, insertion, and deletion operations. This improvement is a milestone in the development of computer science. It is the very first self-balancing binary search tree. It was introduced in 1962 by two Soviet mathematicians, Georgy Adelson-Velsky and Evgenii Landis.[1]

The remainder of this paper will analyse the AVL Tree's properties, discuss the structure and operation of ALE Tree. How is this structure helpful in reducing the depth of the BST tree and resulting in a faster time complexity? Finally, the report discusses implementation details, including code structure, testing strategies, and the specific challenges encountered during development.

## Analysis of Algorithm/Datastructure
Make sure to include the following:
- Time Complexity
- Space Complexity
- General analysis of the algorithm/datastructure

### Time complexity of traditional BST
| Operation | Average Case | Worst Case |
|-----------|-------------|-----------|
| Search | $O(\log N)$ | $O(N)$ |
| Insert | $O(\log N)$ | $O(N)$ |
| Delete | $O(\log N)$ | $O(N)$ |

### Space Complexity of AVL Tree
| Operation | Average Case | Worst Case |
|-----------|-------------|-----------|
| Search | $O(\log N)$ | $O(\log N)$ | 
| Insert | $O(\log N)$ | $O(\log N)$ |
| Delete | $O(\log N)$ | $O(\log N)$ |

### Space Complexity of BST and AVL
| Operation | Space Complexity |
|-----------|-------------|
| Search | $O(N)$ |
| Insert | $O(N)$ |
| Delete | $O(N)$ |
## Empirical Analysis
- What is the empirical analysis?
- Provide specific examples / data.


## Application
- What is the algorithm/datastructure used for?
- Provide specific examples
- Why is it useful / used in that field area?
- Make sure to provide sources for your information.


## Implementation
- What language did you use?
- What libraries did you use?
- What were the challenges you faced?
- Provide key points of the algorithm/datastructure implementation, discuss the code.
- If you found code in another language, and then implemented in your own language that is fine - but make sure to document that.


## Summary
- Provide a summary of your findings
- What did you learn?

## Reference
[1] G. M. Adelson-Velsky and E. M. Landis. 1962. An algorithm for the organization of information. Doklady Akademii Nauk SSSR 146 (1962), 263–266. (English translation: Soviet Math. Dokl. 3, 1259–1263).
