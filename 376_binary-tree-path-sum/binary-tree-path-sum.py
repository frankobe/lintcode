# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/binary-tree-path-sum
@Language: Python
@Datetime: 16-02-05 18:48
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        result = []
        if root is None or root.val is None or target is None:
            return result
        
        self.DFS(root, target, [root.val], result)
        return result
        
    def DFS(self, root, target, path, result):
        if root.left is None and root.right is None:
            if sum(path) == target:
                result.append(list(path))
            
        if root.left is not None:
            path.append(root.left.val)
            self.DFS(root.left, target, path, result)
            path.pop()
            
        if root.right is not None:
            path.append(root.right.val)
            self.DFS(root.right, target, path, result)
            path.pop()
            
            
        