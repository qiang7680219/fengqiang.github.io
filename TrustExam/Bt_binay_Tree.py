#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : guanglinzhou(z00522822)
# @Version : $Id$

"""
实现二叉树的先序、中序、后序、层次遍历方法
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class BinaryTree(object):
    def __init__(self):
        self.res = []

    def get_res(self):
        print(self.res)

    def preorder(self, root):
        # 先序遍历
        if not root:
            return
        self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        # 中序遍历
        if not root:
            return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)

    def postorder(self, root):
        # 后序遍历
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.res.append(root.val)

    def breadth_traverse(self, root):
        # 队列实现层次遍历
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            self.res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def construct_bt():
    root = TreeNode(3)
    r1 = TreeNode(1)
    r2 = TreeNode(5)
    r3 = TreeNode(4)
    r4 = TreeNode(6)
    root.left = r1
    root.right = r2
    r2.left = r3
    r2.right = r4
    return root


bt = BinaryTree()
root = construct_bt()
bt.breadth_traverse(root)
bt.get_res()