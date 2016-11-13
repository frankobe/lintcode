# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/symmetric-binary-tree
@Language: Python
@Datetime: 16-02-16 20:03
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
    @return true if it is a mirror of itself, or false.
    """
    def isSymmetric(self, root):
        # Write your code here
        if root is None:
            return True
        
        return self.cmpSymmetric(root.left, root.right)
        
    def cmpSymmetric(self, A, B):
        if A is None and B is None:
            return True
        
        if A is None or B is None:
            return False
            
        if A.val != B.val:
            return False
            
        return self.cmpSymmetric(A.left, B.right) and self.cmpSymmetric(A.right, B.left)