# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/lowest-common-ancestor
@Language: Python
@Datetime: 15-07-16 18:56
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None or root.val == A.val or root.val == B.val:
            return root
            
        # Divide
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        
        # Conquer
        if left is None and right is None:
            return None
        
        if left is not None and right is None:
            return left
            
        if left is None and right is not None:
            return right
            
        if left is not None and right is not None:
            return root
            
            
