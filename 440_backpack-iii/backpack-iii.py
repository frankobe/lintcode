# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/backpack-iii
@Language: Python
@Datetime: 16-11-03 17:53
'''

class Solution:
    # @param {int[]} A an integer array
    # @param {int[]} V an integer array
    # @param {int} m an integer
    # @return {int} an array
    def backPackIII(self, A, V, m):
        # Write your code here
        
        if m < 0 or not A or not V:
            return 0
            
        
        # dp[i][j] = max(dp[i-1][j], dp[i][j-A[i-1]]+V[i-1])
        n = len(A)
        dp = [[0 for i in xrange(m+1)] for j in xrange(n+1)]
        
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                if j >= A[i-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-A[i-1]]+V[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][m]