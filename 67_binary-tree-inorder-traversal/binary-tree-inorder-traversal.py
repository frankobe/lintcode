# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/binary-tree-inorder-traversal
@Language: Python
@Datetime: 16-02-21 07:27
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
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        return self.helper(root, [])
    
    def helper(self, node, result):
        if node:
            if node.left:
                self.helper(node.left, result)
            
            result.append(node.val)
            
            if node.right:
                self.helper(node.right, result)
            
        return result