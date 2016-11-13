# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/stone-game
@Language: Python
@Datetime: 16-04-25 17:34
'''

class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame(self, A):
        # Write your code here
        if A is None or len(A) == 0:
            return 0
            
        m = len(A)
        self.dp = [[None for i in A] for j in A]
        self.sumdp = [[None for i in A] for j in A]
        # init
        count = 0
        for i in xrange(m):
            self.dp[i][i] = 0
            self.sumdp[0][i] = count + A[i] 
            count = self.sumdp[0][i]
            
        return self.compute(0, m-1, A)
        
    def compute(self, start, end, A):
        if start > end:
            return 0
        
        if self.dp[start][end] is not None:
            return self.dp[start][end]
        
        if self.sumdp[start][end] is None:
            self.sumdp[start][end] = self.sumdp[0][end] - self.sumdp[0][start-1]
        
        smallest = sys.maxint
        for i in xrange(start, end):
            smallest = min(self.compute(start, i, A)+self.compute(i+1, end, A)+self.sumdp[start][end], smallest)
        
        self.dp[start][end] = smallest
        return smallest
            
            
        