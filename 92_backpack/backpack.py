# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/backpack
@Language: Python
@Datetime: 16-11-03 16:35
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        if A is None or len(A) == 0:
            return 0
            
        n = len(A)
        # 1D sliding array, special case for backpack, because dp[i][j] relates 
        # with dp values in up-left area
        dp = [0 for i in xrange(m+1)]
        
        for item in A:
            for j in xrange(m, 0, -1):
                if j >= item :
                    dp[j] = max(dp[j], dp[j-item]+item)
        
        return dp[m]
        
        # 2d dp
        # dp func
        # dp[n][m] = max(dp[n-1][m], dp[n-1][m-A[n]])
        # ***MLE***
        # dp = [[0 for i in xrange(m+1)] for j in xrange(n+1)]
        # for i in xrange(1, n+1):
        #     for j in xrange(1, m+1):
        #         if j >= A[i-1]:
        #             dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]]+A[i-1])
        #         else:
        #             dp[i][j] = dp[i-1][j]
                    
        # return dp[n][m]