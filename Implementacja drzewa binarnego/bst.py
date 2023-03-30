#!/usr/bin/python
# -*- coding: utf-8 -*-

class BSTNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def search_util(self, root, key):
        if root is None:
            return root
        if root.key == key:
            return root.value
        if root.key < key:
            return self.search_util(root.right, key)
        return self.search_util(root.left, key)

    def search(self, key):
        return self.search_util(self.root, key)

    def insert(self, key, val):
        if self.root is None:
            new = BSTNode()
            new.key = key
            new.value = val
            self.root = new
            return
        node = self.root
        prev = None
        while node is not None:
            if node.key < key:
                prev = node
                node = node.right
            elif node.key > key:
                prev = node
                node = node.left
            else:
                node.value = val
                return
        new = BSTNode()
        new.key = key
        new.value = val
        if prev.key < key:
            prev.right = new
        else:
            prev.left = new
        new.parent = prev

    def delete(self, key):
        self.delete_util(self.root, key)

    def delete_util(self, root, key):
        if root is None:
            return root
        if root.key > key:
            root.left = self.delete_util(root.left, key)
        elif root.key < key:
            root.right = self.delete_util(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp = root.right
            mini = temp.key
            val = temp.value
            while temp.left:
                temp = temp.left
                mini = temp.key
                val = temp.value
            root.key = mini
            root.value = val
            root.right = self.delete_util(root.right, root.key)
        return root

    def print_inorder_util(self, root):
        if root is not None:
            self.print_inorder_util(root.left)
            print(str(root.key) + ":" + str(root.value), end="  ")
            self.print_inorder_util(root.right)

    def print_inorder(self):
        self.print_inorder_util(self.root)

    def height_util(self, root):
        if root is None:
            return 0
        else:
            l_side = self.height_util(root.left)
            r_side = self.height_util(root.right)

            if l_side > r_side:
                return l_side + 1
            else:
                return r_side + 1

    def height(self):
        return self.height_util(self.root)

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl + 5)
            print()
            print(lvl * " ", node.key, node.value)
            self._print_tree(node.left, lvl + 5)


tree = BST()

data = {50: 'A', 15: 'B', 62: 'C', 5: 'D', 20: 'E', 58: 'F', 91: 'G', 3: 'H', 8: 'I', 37: 'J', 60: 'K', 24: 'L'}
for i in data:
    tree.insert(i, data[i])
tree.print_tree()

tree.print_inorder()
print("")

print(tree.search(24))

tree.insert(20, "AA")
tree.insert(6, "M")
tree.delete(62)
tree.insert(59, "N")
tree.insert(100, "P")
tree.delete(8)
tree.delete(15)
tree.insert(55, "R")
tree.delete(50)
tree.delete(5)
tree.delete(24)

print(tree.height())

tree.print_inorder()
tree.print_tree()
