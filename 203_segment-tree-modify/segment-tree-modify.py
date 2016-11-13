# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/segment-tree-modify
@Language: Python
@Datetime: 16-09-30 19:04
'''

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:	
    """
    @param root, index, value: The root of segment tree and 
    @ change the node's value with [index, index] to the new given value
    @return: nothing
    """
    def modify(self, root, index, value):
        # write your code here
        if root is None:
            return None
        
        if index not in xrange(root.start, root.end+1):
            return root
        
        if index == root.start == root.end:
            root.max = value
            return root
        
        mid = (root.start+root.end)/2
        if index > mid:
            root.right = self.modify(root.right, index, value)
            root.max = max(root.left.max, root.right.max)
        else:
            root.left = self.modify(root.left, index, value)
            root.max = max(root.left.max, root.right.max)
            
        return root
            
        
        