# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/minimum-depth-of-binary-tree
@Language: Python
@Datetime: 16-02-17 20:32
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
    @return: An integer
    """ 
    def minDepth(self, root):
        # write your code here
        
        if root is None:
            return 0
        
        return self.helper(root, 1)
                
    def helper(self, root, depth):
        if root is None:
            return depth - 1
    
        if root.left is None and root.right is None:
            return depth
        
        if root.left and not root.right:
            return self.helper(root.left, depth + 1)
            
        if not root.left and root.right:
            return self.helper(root.right, depth + 1)
        
        return min(self.helper(root.left, depth + 1), self.helper(root.right, depth + 1))