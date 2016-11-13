# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/binary-tree-preorder-traversal
@Language: Python
@Datetime: 16-10-25 20:12
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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        
        # 1. recurision 
        # result = []
        # self.dfs(root, result)
        # return result
        
        # 2. while
        # return self.bfs(root)
        
        # 3. divide & conquer
        return self.divide(root)
    
    def dfs(self, node, result):
        # top down
        if node is None:
            return
        
        result.append(node.val)
        self.dfs(node.left, result)
        self.dfs(node.right, result)
        
    def bfs(self, root):
        if root is None:
            return []
        
        stack = [root]
        result = []
        
        while len(stack) != 0:
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
            
        return result
        
    def divide(self, root):
        # bottom up
        if root is None:
            return []
        
        rt = []
        
        left = self.divide(root.left)
        right = self.divide(root.right)
    
        rt.append(root.val)
        rt.extend(left)
        rt.extend(right)
        
        return rt
        
    
        
        
        
        
        