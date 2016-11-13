# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/backpack-ii
@Language: Python
@Datetime: 16-11-03 17:46
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # write your code here
        if m < 0 or not A or not V:
            return 0
            
        n = len(A)
        dp = [[0 for i in xrange(m+1)] for j in xrange(n+1)]
        # dp[n][m] = max(dp[n-1][m], dp[n-1][m-A[n]]+V[n])
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                if j >= A[i-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]]+V[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][m]
                