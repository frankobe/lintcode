# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/max-tree
@Language: Python
@Datetime: 15-10-05 21:53
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        # write your code here
        stack = []
        
        for ele in A:
            node = TreeNode(ele)

            while len(stack) != 0 and ele > stack[-1].val:
                node.left = stack.pop()
                
            if len(stack) != 0 and ele < stack[-1].val:
                stack[-1].right = node
            
            stack.append(node)
            
        return stack[0]
            
            
                
            
                
            
            
