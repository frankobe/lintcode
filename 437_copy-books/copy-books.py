# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/copy-books
@Language: Python
@Datetime: 16-11-21 00:51
'''

class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
            
        n = len(pages)
        sum = [0 for i in xrange(n+1)]
        for i in xrange(1, n+1):
            sum[i] = sum[i-1]+pages[i-1]
            
        dp = [[0 for i in xrange(k+1)] for j in xrange(n+1)] 
        
        # i books, j ppl
        # dp[i][j] = min(dp[i-1][j], dp[i-1][j]+pages[i]))
        
        import sys
        for i in xrange(1, n+1):
            dp[i][1] = sum[i]
        
        # non 2 pointer optimization, i and l are two pts
        # for i in xrange(1, n+1):
        #     for j in xrange(2, k+1):
        #         dp[i][j] = dp[i][j-1]
        #         for l in xrange(i):
        #             if dp[l][j-1] < sum[i]- sum[l]:
        #                 dp[i][j] = min(dp[i][j], sum[i]-sum[l])
        #             else:
        #                 dp[i][j] = min(dp[i][j], dp[l][j-1])
        #                 break
        
        for j in xrange(2, k+1):
            # if # of books < # of copier, find the largest book is sufficient
            dp[i][j] = max(pages[0:i])
            l = 1 
            for i in xrange(j+1, n+1):
                dp[i][j] = dp[i][j-1]
                while l < i:
                    if dp[l][j-1] < sum[i] - sum[l]:
                        dp[i][j] = min(dp[i][j], sum[i]-sum[l])
                        l += 1
                    else:
                        dp[i][j] = min(dp[i][j], dp[l][j-1])
                        if l > 2:
                            l -= 1
                        break
        # print dp       
        return dp[n][k]