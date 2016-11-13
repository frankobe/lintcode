# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/binary-tree-maximum-path-sum-ii
@Language: Python
@Datetime: 16-02-01 06:50
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
    @param root the root of binary tree.
    @return an integer
    """
    def maxPathSum2(self, root):
        # Write your code here
        return self.iterator(root, True)
        
    def iterator(self, root, init):
        if root is None:
            return 0
        
        leftsum, rightsum = 0, 0
        if root.left:
            leftsum = self.iterator(root.left, False)
        if root.right:
            rightsum = self.iterator(root.right, False)
            
        if root.val + max(leftsum, rightsum) > 0:
            return root.val + max(leftsum, rightsum)
        elif root.val > 0:
            return root.val
        elif init:
            return root.val
        else:
            return 0