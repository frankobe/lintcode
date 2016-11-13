# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/segment-tree-build-ii
@Language: Python
@Datetime: 16-10-02 03:02
'''

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:	
    # @oaram A: a list of integer
    # @return: The root of Segment Tree
    def build(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return None
            
        return self.helper(0, len(A)-1, A)
    
    def helper(self, start, end, A):
        if start > end:
            return None
        node = SegmentTreeNode(start, end, None)
        if start == end:
            node.max = A[start]
        else:
            mid = (start+end)/2
            node.left = self.helper(start, mid, A)
            node.right = self.helper(mid+1, end, A)
            node.max = max(node.left.max, node.right.max)
        
        return node
        
        