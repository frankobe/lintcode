# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/kth-smallest-sum-in-two-sorted-arrays
@Language: Python
@Datetime: 16-09-29 21:21
'''

from heapq import *
class Solution:
    # @param {int[]} A an integer arrays sorted in ascending order
    # @param {int[]} B an integer arrays sorted in ascending order
    # @param {int} k an integer
    # @return {int} an integer
    def kthSmallestSum(self, A, B, k):
        # Write your code here
        heap = []
        
        col, row = len(A), len(B)
        l = min(col, k)
        for i in xrange(l):
            heappush(heap, (A[i]+B[0], i, 0))
            
        for i in xrange(k-1):
            node = heappop(heap)
            x, y = node[1], node[2]
            if y+1 < row:
                heappush(heap, (A[x]+B[y+1], x, y+1))
                    
        return heap[0][0]
                