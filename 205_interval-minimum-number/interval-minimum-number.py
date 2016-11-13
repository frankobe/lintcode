# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/interval-minimum-number
@Language: Python
@Datetime: 16-09-30 20:06
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class SegTreeNode(object):
    def __init__(self, start, end, min=None):
        self.start, self.end, self.min = start, end, min
        self.left, self.right = None, None
        
class Solution:	
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """
    def intervalMinNumber(self, A, queries):
        # write your code here
        if A is None or len(A) == 0:
            return None
            
        if queries is None or len(queries) == 0:
            return []
            
        root = self.buildSegTree(A, 0, len(A)-1)
        result = []
        
        for q in queries:
            result.append(self.querySegTree(root, q.start, q.end))
            
        return result
        
        
    def buildSegTree(self, A, start, end):
        node = SegTreeNode(start, end)
        if start == end:
            node.min = A[start]
            return node
        
        mid = (start+end)/2
        node.left = self.buildSegTree(A, start, mid)
        node.right = self.buildSegTree(A, mid+1, end)
        node.min = min(node.left.min, node.right.min)
        return node
        
    def querySegTree(self, root, start, end):
        if root.start == start and root.end == end:
            return root.min
            
        mid = (root.start+root.end)/2
        if end <= mid:
            return self.querySegTree(root.left, start, end)
        elif start > mid:
            return self.querySegTree(root.right, start, end)
        else:
            return min(self.querySegTree(root.left, start, mid),
                    self.querySegTree(root.right, mid+1, end))
        
        