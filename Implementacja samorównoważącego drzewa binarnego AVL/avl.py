#!/usr/bin/python
# -*- coding: utf-8 -*-

class AVLTreeNode:
    def __init__(self, key=None, val=None, bf=0):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.bf = bf   # współczynnik wyważenia
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        self.root = self._insert(self.root, key, val)

    def _insert(self, root, key, val):
        if not root:
            return AVLTreeNode(key, val, bf=0)
        if key < root.key:
            left_sub_root = self._insert(root.left, key, val)
            root.left = left_sub_root
            left_sub_root.parent = root
        elif key > root.key:
            right_sub_root = self._insert(root.right, key, val)
            root.right = right_sub_root
            right_sub_root.parent = root
        else:
            return root

        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.bf = self._get_height(root.left) - self._get_height(root.right)
        return self.rebalance(root)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            left_sub_root = self._delete(root.left, key)
            root.left = left_sub_root
            if left_sub_root:
                left_sub_root.parent = root
        elif key > root.key:
            right_sub_root = self._delete(root.right, key)
            root.right = right_sub_root
            if right_sub_root:
                right_sub_root.parent = root

        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp = root.right
            mini = temp.key
            minv = temp.val
            while temp.left:
                temp = temp.left
                mini = temp.key
                minv = temp.val
            root.key = mini
            root.val = minv
            root.right = self._delete(root.right, root.key)

        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.bf = self._get_height(root.left) - self._get_height(root.right)
        return self.rebalance(root)

    def search_util(self, root, key):
        if root is None:
            return root
        if root.key == key:
            return root.val
        if root.key < key:
            return self.search_util(root.right, key)
        return self.search_util(root.left, key)

    def search(self, key):
        return self.search_util(self.root, key)


    def rebalance(self, root):
        if root.bf == 2:
            if root.left.bf < 0:  # L-R
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
            else:  # L-L
                return self.rotate_right(root)
        elif root.bf == -2:
            if root.right.bf > 0:  # R-L
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
            else:  # R-R
                return self.rotate_left(root)
        else:
            return root

    def rotate_right(self, root):
        pivot = root.left  # set up pointers
        tmp = pivot.right

        pivot.right = root
        pivot.parent = root.parent
        root.parent = pivot

        root.left = tmp
        if tmp:
            tmp.parent = root

        if pivot.parent:
            if pivot.parent.left == root:
                pivot.parent.left = pivot
            else:
                pivot.parent.right = pivot


        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.bf = self._get_height(root.left) - self._get_height(root.right)

        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1
        pivot.bf = self._get_height(pivot.left) - self._get_height(pivot.right)
        return pivot

    def rotate_left(self, root: AVLTreeNode) -> AVLTreeNode:
        pivot = root.right
        tmp = pivot.left

        pivot.left = root
        pivot.parent = root.parent
        root.parent = pivot

        root.right = tmp
        if tmp:
            tmp.parent = root

        if pivot.parent:
            if pivot.parent.left == root:
                pivot.parent.left = pivot
            else:
                pivot.parent.right = pivot

        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.bf = self._get_height(root.left) - self._get_height(root.right)

        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1
        pivot.bf = self._get_height(pivot.left) - self._get_height(pivot.right)
        return pivot

    def _get_height(self, root):
        if not root:
            return 0
        else:
            return root.height

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl + 5)
            print()
            print(lvl * " ", node.key, node.val)
            self._print_tree(node.left, lvl + 5)

    def print_inorder_util(self, root):
        if root is not None:
            self.print_inorder_util(root.left)
            print(str(root.key) + ":" + str(root.val), end="  ")
            self.print_inorder_util(root.right)

    def print_inorder(self):
        self.print_inorder_util(self.root)
        print()

Tree = AVLTree()
data = {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'}
for i in data:
    Tree.insert(i, data[i])
Tree.print_tree()
Tree.print_inorder()
print(Tree.search(10))
Tree.delete(50)
Tree.delete(52)
Tree.delete(11)
Tree.delete(57)
Tree.delete(1)
Tree.delete(12)
Tree.insert(3, 'AA')
Tree.insert(4, 'BB')
Tree.delete(7)
Tree.delete(8)
Tree.print_tree()
Tree.print_inorder()
