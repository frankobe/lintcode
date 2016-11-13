# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/sliding-window-matrix-maximum
@Language: Python
@Datetime: 16-11-04 18:26
'''

import sys
class Solution:
    # @param {int[][]} matrix an integer array of n * m matrix
    # @param {int} k an integer
    # @return {int} the maximum number
    def maxSlidingMatrix(self, matrix, k):
        # Write your code here
        
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        if k > m or k > n:
            return 0
        
        sumM = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
        
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                    sumM[i][j] = matrix[i-1][j-1] + sumM[i-1][j] \
                                + sumM[i][j-1] - sumM[i-1][j-1]
                                
        maxVal = -sys.maxint
        for i in xrange(1, m+1 - (k-1)):
            for j in xrange(1, n+1 - (k-1)):
                tmpVal = sumM[i-1][j-1] + sumM[i+k-1][j+k-1] \
                        - sumM[i+k-1][j-1] - sumM[i-1][j+k-1]
                maxVal = max(maxVal, tmpVal)
        
        if maxVal == -sys.maxint:
            return 0
        return maxVal