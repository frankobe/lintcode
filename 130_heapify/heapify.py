# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/heapify
@Language: Python
@Datetime: 16-10-27 16:56
'''

class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        for i in xrange(len(A)):
            self._siftup(i, A)
        
    def _swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def _siftup(self, nodeIdx, heap):
        parentIdx = (nodeIdx + 1)/2 - 1
        while parentIdx >= 0 and heap[parentIdx] > heap[nodeIdx]:
            self._swap(parentIdx, nodeIdx, heap)
            nodeIdx = parentIdx
            parentIdx = (nodeIdx+1)/2 - 1
        
        
        