# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/longest-increasing-continuous-subsequence-ii
@Language: Python
@Datetime: 16-04-24 07:26
'''

class Solution:
    # @param {int[][]} A an integer matrix
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequenceII(self, A):
        # Write your code here        
        if A is None:
            return 0
        
        self.m = len(A)
        if self.m == 0:
            return 0
            
        self.n = len(A[0])
        if self.n == 0:
            return 0
            
        self.dp = [[0 for i in xrange(self.n)] for j in xrange(self.m)]
        
        
        for i in xrange(self.m):
            for j in xrange(self.n):
                self.dfs(i, j, A)
                
        return max(max(row) for row in self.dp)
        
    def dfs(self, x, y, A):
        if self.dp[x][y] != 0:
            return self.dp[x][y]
            
        direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        longest = 1
        for d in xrange(4):
            nx = x+direct[d][0]
            ny = y+direct[d][1]
            
            if nx < 0 or nx >= self.m or ny < 0 or ny >= self.n:
                continue
                
            if A[nx][ny] > A[x][y]:
                longest = max(self.dfs(nx, ny, A)+1, longest)
        self.dp[x][y] = longest
        return self.dp[x][y]
            
            
                
        