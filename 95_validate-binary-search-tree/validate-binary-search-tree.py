# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/validate-binary-search-tree
@Language: Python
@Datetime: 15-07-15 19:41
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
    @return: True if the binary tree is BST, or false
    """  
    def validBSTHelper(self, root, low, high):
        if root is None:
            return True
            
        if root.val >= high or root.val <= low:
            return False
        
        return self.validBSTHelper(root.left, low, min(root.val, high)) and self.validBSTHelper(root.right, max(root.val, low), high)
            
    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True
            
        return self.validBSTHelper(root, -sys.maxint, sys.maxint)
        
