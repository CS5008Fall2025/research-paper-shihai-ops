[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zBqi0PeJ)
# Research Paper
* Name: Haisheng Shi
* Semester: Fall 2025
* Topic: AVL Tree and its comparison with BST Tree. 



Note the following is an example outline to help you. Please rework as you need, you do not need to follow the section heads and *YOU SHOULD NOT* make everything a bulleted list. This needs to read as an executive report/research paper. 

## Introduction
This paper focuses on the properties of the AVL Tree and its implementation. The AVL tree is one of the most important data structures invented by Georgy Adelson-Velsky and Evgenii Landis	in 1962. It creatively resolved the problem of BST(Binary Search Tree) when processing well-sorted data. In this case, the BST will degrade to a linked list, and the time complexity of search, insert and delete would be $O(n)$. To solve this problem, the AVL tree introduces a self-balancing property where the heights of the two child subtrees of any node differ by at most one (known as the Balance Factor). If this property is violated during an insertion or deletion, the tree automatically restores balance through a series of rotation operations (Left, Right, Left-Right, or Right-Left). This mechanism guarantees that the tree height always remains logarithmic relative to the number of nodes, ensuring a time complexity of $O(\log n)$ for search, insertion, and deletion operations. 

 For arbitrary node V in AVL Tree, The Balance Factor $$BF(v) = H(v_{left}) - H(v_{right})$$, and $$|BF(v)| \le 1$$

 $$H(v) = 
\begin{cases} 
-1 & \text{if } v \text{ is null} \\
1 + \max(H(v_{left}), H(v_{right})) & \text{otherwise}
\end{cases}$$

This improvement is a milestone in the development of computer science. It is the very first self-balancing binary search tree in history. It was introduced in 1962 by two Soviet mathematicians, Georgy Adelson-Velsky and Evgenii Landis.[1]
                   
 

The remainder of this paper will analyse the AVL Tree's properties, discuss the structure and operation of the AVL Tree. How is this structure helpful in reducing the depth of the BST tree and resulting in a faster time complexity? Finally, the report discusses implementation details, including code structure, testing strategies, and the specific challenges encountered during development.

## Analysis of Algorithm/Datastructure
Make sure to include the following:

### Time complexity of traditional BST
| Operation |Best Case| Average Case | Worst Case |
|-----------|---|-------------|-----------|
| Search | $O(\log N)$ | $O(\log N)$ | $O(N)$ |
| Insert | $O(\log N)$ | $O(\log N)$ | $O(N)$ |
| Delete | $O(\log N)$ | $O(\log N)$ | $O(N)$ |

### Time Complexity of AVL Tree
| Operation |Best Case| Average Case | Worst Case |
|-----------|-------------|-----------|---|
| Search | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | 
| Insert | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ |
| Delete | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ |

### Space Complexity of BST and AVL
| BST | AVL |
|-------------|-------------|
| $O(N)$ | $O(N)$ |

From the forms above, it is clearly to see that both BST and AVL tree has an average of $O(\log N)$ for time complexity. However, the more sorted data samples that the BST receives, the slower the BST becomes.
When handling a random sequence of sample data, both BST and AVL have $O(\log N)$ of time complexity. It is because the time complexity of tree operations is directly proportional to the height of the tree. If the data sample is highly randomized, both the left and right children would have a similar chance to be used to store data; hence, the tree is mostly balanced, making the feature of AVL, such as get_balance(node)， rotate, unnecessary. 

```python
# insert data into bst recursively. 
 def insert(self, key):
        if self.root is None: 
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

def _insert(self, node, key):
        if key < node.key:  # If and else block would be in a highly randomized sample data, their chance of being used is similar. 
            if node.left is None:
                node.left = BSTNode(key)# 
            else:
                self._insert(node.left, key)
        else: # If and else block would be in a highly randomized sample data, their chance of being used is similar. 
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert(node.right, key)
```

When handling a well-sorted data sample, the BST will degrade to a linked list. Leafs no longer exist. Let us insert [1, 2, 3, 4, 5] inside the BST. As the code shows below, let's begin with 1. 1 will be stored in the root， then insert 2, 2 > 1, the ``` else:``` block will be executed, and add 2 at the right side of the tree branch. Then we insert 3, 3 > 2, and add 3 to the right child. Same for all monotonic increasing elements, all left children will stay empty. Similarly, for a monotonic decreasing data sample, the  ```if key < node.key: ``` will always be executed and always store data at the left child, and all right children will stay empty, making the BST degrade to a linked list. Hence, the time complexity of this case would be the same as a linked list. 
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
In comparison, the AVL tree will automatically detect this imbalance using the balance factor, which tracks the height difference between the left and right subtrees. When sorted data (e.g., [1, 2, 3, 4, 5]) is inserted, the AVL tree recognizes that the tree is becoming right-heavy (balance factor < -1). It immediately triggers a ```left_rotate``` to restructure the nodes, reduce the height, and ensure the root remains a median value rather than the smallest element.
```python
# Check if the right is too heavy and input is larger than the current right children.
    if balance < -1 and key > node.right.key:
        return self.left_rotate(node) #If it is true, perform left rotation.

    def left_rotate(self, z):
        y = z.right #y is the future new root node and current right child of z
        T2 = y.left # Old left child of y. 
        y.left = z # y goes to the root and z becomes the left child of y
        z.right = T2 # T2 becomes the right child of z
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))# update the height of the tree
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

```

## Empirical Analysis
- What is the empirical analysis?
- Provide specific examples/data.
The forms of tree height versus the sample size of random, reverse-sorted, and ascending-sorted are shown below. In sorted and reversed form, BST is not included after n=2000 since it is too slow and will make the following line chart harder to read. 
[analysis_random_height](analysis_random_height.csv), 
[analysis_reverse_sorted_height](analysis_reverse_sorted_height.csv), 
[analysis_sorted_height](analysis_sorted_height.csv).

The forms of time spent to form a tree versus the sample size of random, reverse-sorted, and ascending-sorted are shown below. In sorted and reversed form, the regular BST is not included after n=2000 since it is too slow and will make the following line chart harder to read. 
[analysis_random_runtime](analysis_random_runtime.csv),
[analysis_reverse_sorted_runtime](analysis_reverse_sorted_runtime.csv),
[analysis_sorted_runtime](analysis_sorted_runtime.csv).




### Time Complexity comparison
The data of the time consumed by generating a BST and an AVL tree, and the height of BST and AVL have shown below. 
![analysis_random](analysis_random.png)
In the random case, the BST costs less time than AVL. It is because the AVL needs to check the height of its left and right children and calculate the balance factor, and check whether to perform rotation or not when inserting a new node into the AVL tree. Although the height of AVL is slightly lower than the BST, but BST performs fewer steps during each insertion, making it slightly faster to build a tree in a random sequence dataset. The height of BST and AVL both grow at logarithmic speed. 
![analysis_reverse](analysis_reverse.png)
![analysis_sorted](analysis_sorted.png)
The height of the BST is equal to the number of inputs for both the reversed and the ascending sequence. While the height of AVL is highly correlated with the log2(n) function, showing that the height of the AVL tree has a logarithmic growth rate along with the input size for both sorted ascending and descending datasets. 
![analysis_reverse2](analysis_reverse2.png)
![analysis_sorted2](analysis_sorted2.png)
The total time consumed to build a tree equals to add of every single time cost by every insertion. For a tree that contains N nodes, the worst-case BST cost is 
$$\text{Total Time} = \sum_{i=1}^{N} i = \frac{N(N+1)}{2} \approx O(N^2)$$
The average case of BST and AVL cost is 
$$\sum_{i=1}^{N} \log i = \log(N!) \approx N \log (N)$$
## Application
- What is the algorithm/data structure used for?
- Provide specific examples
- Why is it useful / used in that field area?
- Make sure to provide sources for your information.
The AVL tree is primarily used to search data. Its property is particularly good at dealing with frequent searches on data that is dynamic(Requires frequent insertions and deletions). Because it enforces strict balancing, it guarantees $O(\log N)$ time complexity for lookup operations, making it much faster than standard Binary Search Trees (BSTs) in read-heavy scenarios where worst-case performance is not acceptable. [1].
In a database, scan operation could be too slow if run in time complexity of O(n). AVL trees are often chosen over other structures because their strict balancing results in shorter average path lengths, optimizing lookup speed at the cost of slightly slower insertion in a highly randomized dataset. [2]
The Windows NT kernel uses AVL tree structures in its Virtual Address Descriptor (VAD) tree to manage the virtual memory address space of processes. [3]

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
[2] Ben Pfaff. 2004. Performance analysis of BSTs in system software. ACM SIGMETRICS Performance Evaluation Review 32, 1 (June 2004), 410–411.
[3] Mark Russinovich and David A. Solomon. 2005. Microsoft Windows Internals (4th ed.). Microsoft Press, Redmond, WA, USA.
