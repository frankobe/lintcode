# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/maximal-square
@Language: Python
@Datetime: 16-10-06 07:05
'''

class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for i in xrange(col+1)] for j in xrange(row+1)]
        
        maxVal = 0
        for i in xrange(1, row+1):
            for j in xrange(1, col+1):
                if matrix[i-1][j-1] == 0:
                    dp[i][j] == 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    maxVal = max(maxVal, dp[i][j])
        return maxVal*maxVal
        