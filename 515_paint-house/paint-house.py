# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/paint-house
@Language: Python
@Datetime: 16-03-29 04:16
'''

class Solution:
    # @param {int[][]} costs n x 3 cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCost(self, costs):
        # Write your code here
        n = len(costs)
        if n < 1:
            return 0
    
        r = [[-1 for i in xrange(3)] for j in xrange(n)]
        
        for i in xrange(3):
            r[0][i] = costs[0][i]
        
        
        for i in xrange(1, n):
            for j in xrange(3):
                r[i][j] = min(r[i-1][(j+1)%3] + costs[i][j],
                            r[i-1][(j+2)%3] + costs[i][j])
                            
        return min(r[n-1])
        