# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/balanced-binary-tree
@Language: Python
@Datetime: 16-10-25 23:56
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
    @return: True if this Binary tree is Balanced, or false.
    """
    
    def isBalanced(self, root):
        # write your code here

        balanced, _ = self.validate(root)
        
        return balanced
        
    def validate(self, root):
        
        if root is None:
            return True, 0
        
        balanced, leftDepth = self.validate(root.left)
        if not balanced:
            return False, leftDepth
        
        balanced, rightDepth = self.validate(root.right)
        if not balanced:
            return False, rightDepth
        
        return abs(leftDepth-rightDepth) <= 1, max(leftDepth, rightDepth)+1