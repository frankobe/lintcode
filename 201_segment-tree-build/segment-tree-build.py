# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/segment-tree-build
@Language: Python
@Datetime: 16-09-30 17:54
'''

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""

class Solution:	
    # @param start, end: Denote an segment / interval
    # @return: The root of Segment Tree
    def build(self, start, end):
        # write your code here
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start, end)
        
        node = SegmentTreeNode(start, end)
        mid = (start+end)/2
        node.left = self.build(start, mid)
        node.right = self.build(mid+1,end)
        
        return node
        

