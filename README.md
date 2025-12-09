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
This study focuses on the properties of the AVL Tree and its implementation. The AVL tree is one of the most important data structures invented by Georgy Adelson-Velsky and Evgenii Landis	in 1962. It creatively resolved the problem of BST(Binary Search Tree) when processing well-sorted data. In this case, the BST will degrade to a linked list and the time complexity of search, insert and delete would be $O(n)$. To solve this problem, the AVL tree introduces a self-balancing property where the heights of the two child subtrees of any node differ by at most one (known as the Balance Factor). If this property is violated during an insertion or deletion, the tree automatically restores balance through a series of rotation operations (Left, Right, Left-Right, or Right-Left). This mechanism guarantees that the tree height always remains logarithmic relative to the number of nodes, ensuring a time complexity of $O(\log n)$ for search, insertion, and deletion operations. This improvement is a milestone in the development of computer science. It is the very first self-balancing binary search tree in history. It was introduced in 1962 by two Soviet mathematicians, Georgy Adelson-Velsky and Evgenii Landis.[1]

The remainder of this paper will analyse the AVL Tree's properties, discuss the structure and operation of the AVL Tree. How is this structure helpful in reducing the depth of the BST tree and resulting in a faster time complexity? Finally, the report discusses implementation details, including code structure, testing strategies, and the specific challenges encountered during development.

## Analysis of Algorithm/Datastructure
Make sure to include the following:
- Time Complexity
- Space Complexity
- General analysis of the algorithm/data structure

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
| BST | AVL |
|-------------|-------------|
| $O(N)$ | $O(N)$ |

From the forms above, it is clearly to see that both BST and AVL tree has an average of $O(\log N)$ for time complexity. However, for more sorted data sample that the BST receives, the slower the BST becomes. When handling a well-sorted data sample, the BST will degrade to a linked list. Leafs no longer exist. Let us insert [1, 2, 3, 4, 5] inside the BST. As the code shows below, let's begin with 1. 1 will be stored in the root， then insert 2, 2 > 1, the ``` else:``` block will be executed, and add 2 at the right side of the tree branch. Then we insert 3, 3 > 2, and add 3 to the right child. Same for all monotonic increasing elements, all left children will stay empty. Similarly, for a monotonic decreasing data sample, the  ```if key < node.key: ``` will always be executed and always store data at the left child, and all right children will stay empty, making the BST become a linked list. 
```python
# insert data into bst recursively. 
 def insert(self, key):
        if self.root is None: 
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

def _insert(self, node, key):
        if key < node.key:  # always store data here if the data sample is monotonic decreasing. 
            if node.left is None:
                node.left = BSTNode(key)# 
            else:
                self._insert(node.left, key)
        else: # always store data here if the data sample is monotonic increasing. 
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert(node.right, key)
```
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
