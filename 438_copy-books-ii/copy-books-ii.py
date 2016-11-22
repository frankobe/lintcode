# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/copy-books-ii
@Language: Python
@Datetime: 16-11-21 07:13
'''

class Solution:
    # @param n: an integer
    # @param times: a list of integers
    # @return: an integer
    def copyBooksII(self, n, times):
        # write your code here
        if n <= 0 or not times:
            return 0
            
        # dp func: dp[i][j] = min(dp[i][j-1], max(dp[k][j-1], (i-k)*times[j-1])
        # find the optimized k
        # Solution 1: DP TLE            
        # m = len(times)
        # dp = [[0 for i in xrange(m+1)] for j in xrange(n+1)]
        
        # import sys
        # for i in xrange(1,n+1):
        #     dp[i][0] = sys.maxint
        #     dp[i][1] = i*times[0]
            
        # for j in xrange(1, m+1):
        #     dp[1][j] = min(times[:j])
        

        # for j in xrange(2, m+1):
        #     k = 1 
        #     for i in xrange(2, n+1):
        #         dp[i][j] = dp[i][j-1]
        #         while k < i+1:
        #             if dp[i-k][j-1] > k*times[j-1]:
        #                 dp[i][j] = min(dp[i][j], dp[i-k][j-1])
        #                 k += 1
        #             else:
        #                 dp[i][j] = min(dp[i][j], k*times[j-1])
        #                 if k > 1:
        #                     k -= 1
        #                 break
        # return dp[n][m]
        
        # BST
        import heapq
        h = []
        for a in times:
            heapq.heappush(h, (a, a))
        
        for i in xrange(n):
            total, cost = heapq.heappop(h)
            heapq.heappush(h, (total+cost, cost))
            
        result = -1
        for (total, cost) in h:
            if total > cost:
                result = max(result, total-cost)
            
        return result
        
        
        