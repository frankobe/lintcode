# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/paint-house-ii
@Language: Python
@Datetime: 16-03-29 05:03
'''

class Solution:
    # @param {int[][]} costs n x k cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCostII(self, costs):
        # Write your code here
        n = len(costs)
        if n < 1:
            return 0
        
        k = len(costs[0])
        if k < 1:
            return 0
        
        r = [[0 for i in xrange(k)] for j in xrange(n)]
        min1, min2 = -1, -1
        for i in xrange(k):
            r[0][i] = costs[0][i]
            if min1 < 0 or r[0][i] < r[0][min1]:
                min2 = min1
                min1 = i
            elif min2 < 0 or r[0][i] < r[0][min2]:
                min2 = i
            
        for i in xrange(1, n):
            last1, last2 = min1, min2
            min1, min2 = -1, -1
            for j in xrange(k):
                if j == last1:
                    r[i][j] = r[i-1][last2] + costs[i][j]
                else:
                    r[i][j] = r[i-1][last1] + costs[i][j]
                    
                if min1 < 0 or r[i][j] < r[i][min1]:
                    min2 = min1
                    min1 = j
                elif min2 < 0 or r[i][j] < r[i][min2]:
                    min2 = j
                    
        return r[n-1][min1]