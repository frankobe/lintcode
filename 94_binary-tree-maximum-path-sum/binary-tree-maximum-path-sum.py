# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/binary-tree-maximum-path-sum
@Language: Python
@Datetime: 16-10-26 18:13
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
    
    def maxPathSum(self, root):
        # write your code here
        max,_ = self.helper(root)
        return max
        
    
    def helper(self, root):
        if root is None:
            return -sys.maxint, 0
            
        lmax, lsingle = self.helper(root.left)
        rmax, rsingle= self.helper(root.right)
        
        maxPathSum = max(lmax, rmax, lsingle+root.val+rsingle)
        single = max(lsingle+root.val, rsingle+root.val, root.val, 0)
        
        return maxPathSum, single
        
        