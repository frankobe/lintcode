# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/segment-tree-query
@Language: Python
@Datetime: 16-09-30 18:42
'''

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:	
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The maximum number in the interval [start, end]
    def query(self, root, start, end):
        # write your code here
        
        if root is None:
            return None
            
        if end < root.start or start > root.end:
            return None
        
        mid = (root.start+root.end)/2
        
        if start <= root.start and end >= root.end:
            return root.max
        elif start > mid:
            return self.query(root.right, start, min(end, root.end))
        elif end <= mid:
            return self.query(root.left, max(start, root.start), end)
        else:
            return max(self.query(root.left, max(start, root.start), mid), \
                    self.query(root.right, mid+1, min(end, root.end)))