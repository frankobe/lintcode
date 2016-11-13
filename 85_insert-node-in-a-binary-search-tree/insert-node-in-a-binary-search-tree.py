# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/insert-node-in-a-binary-search-tree
@Language: Python
@Datetime: 15-07-15 18:07
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode1(self, root, node):
        # write your code here
        if root is None:
            return node
        
        if root.val > node.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
            
        return root
        
    def insertNode(self, root, node):
          
        if root is None:
            return node
            
        tmp = root
        last = None
        
        while tmp is not None:
            last = tmp
            if tmp.val > node.val:
                tmp = tmp.left
            else:
                tmp = tmp.right
        
        if last.val > node.val:
            last.left = node
        else:
            last.right = node
        
        return root
            
            