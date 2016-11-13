# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/complete-binary-tree
@Language: Python
@Datetime: 16-02-17 00:36
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root, the root of binary tree.
    @return true if it is a complete binary tree, or false.
    """
    def isComplete(self, root):
        # Write your code here
        if root is None:
            return True
        
        count = self.countNode(root)
        return self.iterator(root,0, count)
        
    def countNode(self, root):
        if root is None:
            return 0
        
        return 1 + self.countNode(root.left)+self.countNode(root.right)
        
    def iterator(self, root, idx, count):
        # BFS
        if root is None:
            return True
        
        if idx >= count:
            return False
        
        return self.iterator(root.left, idx*2 + 1, count) and self.iterator(root.right, idx*2+2, count)
        
        