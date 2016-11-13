# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/kth-smallest-number-in-sorted-matrix
@Language: Python
@Datetime: 16-09-29 19:03
'''

from heapq import *

class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        heap = []
        col, row = len(matrix[0]), len(matrix)
        for i in xrange(col):
             heappush(heap, (matrix[0][i], 0, i))
            
        for i in xrange(k-1):
            cur = heappop(heap)
            x, y = cur[1], cur[2]
            if x+1 < row:
                heappush(heap, (matrix[x+1][y], x+1, y))
            
        return heap[0][0]
        