# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/tweaked-identical-binary-tree
@Language: Python
@Datetime: 16-02-16 09:10
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
    @param a, b, the root of binary trees.
    @return true if they are tweaked identical, or false.
    """
    def isTweakedIdentical(self, a, b):
        # Write your code here
        
        if a is None and b is None:
            return True
        
        if a is None or b is None:
            return False
        
        if a.val != b.val:
            return False
            
        if self.isTweakedIdentical(a.left, b.left) and self.isTweakedIdentical(a.right, b.right):
            return True
            
        if self.isTweakedIdentical(a.left, b.right) and self.isTweakedIdentical(a.right, b.left):
            return True
        
        return False