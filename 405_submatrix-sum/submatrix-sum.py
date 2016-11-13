# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/submatrix-sum
@Language: Python
@Datetime: 16-10-12 19:33
'''

class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        # Write your code here
        if matrix is None or len(matrix) == 0 \
            or matrix[0] is None or len(matrix[0]) == 0:
                return []
                
        m, n = len(matrix), len(matrix[0])
        
        sumM = [[0 for i in xrange(n+1)] for j in xrange(m+1)]
    
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                sumM[i][j] = sumM[i-1][j] + sumM[i][j-1] - sumM[i-1][j-1] + \
                            matrix[i-1][j-1]
                for p in xrange(i):
                    for q in xrange(j):
                        if sumM[i][j] - sumM[i][q] == sumM[p][j] - sumM[p][q]:
                            return [(p, q), (i-1, j-1)]
                            
                            
        return []