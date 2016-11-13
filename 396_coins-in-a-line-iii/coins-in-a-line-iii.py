# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/coins-in-a-line-iii
@Language: Python
@Datetime: 16-04-25 04:13
'''

class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        # dp[i][j] = max(pick_left, pick_right)
        
        if values is None or len(values) < 2:
            return True
            
        self.dp = [[None for i in values] for j in values]
        self.values = values
        
        for i in xrange(len(values)):
            self.dp[i][i] = values[i]
            
        target = sum(values)/2.0
        
        return self.compute(0, len(values)-1) > target
        
    def compute(self, start, end):
        if start > end:
            return 0
        
        if self.dp[start][end] is not None:
            return self.dp[start][end]
            
        pickLeft = self.values[start] + min(self.compute(start+2, end), self.compute(start+1, end-1))
        pickRight = self.values[end] + min(self.compute(start, end-2), self.compute(start+1, end-1))
        self.dp[start][end] = max(pickLeft, pickRight)
        return self.dp[start][end]