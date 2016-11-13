# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/binary-search-tree-iterator
@Language: Python
@Datetime: 15-07-22 19:06
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = Solution(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""
class Solution:
    #@param root: The root of binary tree.
    def __init__(self, root):
        # write your code here
        self.tree = []
        self.pushLeft(root)
        
    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        return self.tree
    #@return: return next node
    def next(self):
        #write your code here
        node = self.tree.pop()
        self.pushLeft(node.right)
        return node

    def pushLeft(self, root):
        if root is None:
            return
        
        self.tree.append(root)
        self.pushLeft(root.left)