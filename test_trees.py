import unittest
import random
from trees import BSTTree, AVLTree


class TestBSTTree(unittest.TestCase):
    def setUp(self):
        self.bst = BSTTree()

    def test_empty_tree(self):
        self.assertEqual(self.bst.get_height(), 0)

    def test_basic_insertion(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertEqual(self.bst.root.key, 10)
        self.assertEqual(self.bst.root.left.key, 5)
        self.assertEqual(self.bst.root.right.key, 15)
        self.assertEqual(self.bst.get_height(), 2)

    def test_worst_case_sorted(self):
        for i in range(1, 6):
            self.bst.insert(i)

        self.assertEqual(self.bst.get_height(), 5)
        self.assertEqual(self.bst.root.key, 1)
        self.assertEqual(self.bst.root.right.key, 2)


class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.avl = AVLTree()

    def check_balance(self, node):
        if node is None:
            return True

        l_h = self.avl.get_height(node.left)
        r_h = self.avl.get_height(node.right)
        balance = l_h - r_h

        if abs(balance) > 1:
            return False

        return self.check_balance(node.left) and self.check_balance(node.right)

    def check_bst_property(self, node, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True

        if not (min_val < node.key < max_val):
            return False

        return (self.check_bst_property(node.left, min_val, node.key) and
                self.check_bst_property(node.right, node.key, max_val))

    def test_rr_rotation(self):
        self.avl.insert(1)
        self.avl.insert(2)
        self.avl.insert(3)
        self.assertEqual(self.avl.root.key, 2)
        self.assertEqual(self.avl.root.left.key, 1)
        self.assertEqual(self.avl.root.right.key, 3)
        self.assertEqual(self.avl.get_tree_height(), 2)

    def test_ll_rotation(self):
        self.avl.insert(3)
        self.avl.insert(2)
        self.avl.insert(1)
        self.assertEqual(self.avl.root.key, 2)
        self.assertEqual(self.avl.get_tree_height(), 2)

    def test_rl_rotation(self):
        self.avl.insert(1)
        self.avl.insert(3)
        self.avl.insert(2)
        self.assertEqual(self.avl.root.key, 2)
        self.assertEqual(self.avl.root.left.key, 1)
        self.assertEqual(self.avl.root.right.key, 3)
        self.assertEqual(self.avl.get_tree_height(), 2)

    def test_lr_rotation(self):
        self.avl.insert(3)
        self.avl.insert(1)
        self.avl.insert(2)
        self.assertEqual(self.avl.root.key, 2)
        self.assertEqual(self.avl.root.left.key, 1)
        self.assertEqual(self.avl.root.right.key, 3)
        self.assertEqual(self.avl.get_tree_height(), 2)

    def test_large_sorted_input(self):
        n = 100
        for i in range(n):
            self.avl.insert(i)
        height = self.avl.get_tree_height()
        self.assertTrue(height < 15, f"AVL Tree height {height} is too large for {n} nodes!")
        self.assertTrue(self.check_balance(self.avl.root), "Tree is unbalanced at some node")
        self.assertTrue(self.check_bst_property(self.avl.root), "BST property violated")

    def test_random_fuzzing(self):
        data = list(range(1000))
        random.shuffle(data)

        for num in data:
            self.avl.insert(num)

        self.assertTrue(self.check_balance(self.avl.root), "Random fuzzing caused imbalance")
        self.assertTrue(self.check_bst_property(self.avl.root), "Random fuzzing violated BST property")


if __name__ == '__main__':
    print("Running tests for trees.py...")
    unittest.main()