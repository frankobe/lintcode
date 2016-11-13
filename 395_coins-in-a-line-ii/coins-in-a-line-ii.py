# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/coins-in-a-line-ii
@Language: Python
@Datetime: 16-04-25 03:56
'''

class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        if values is None or len(values) < 3:
            return True
        
        target =  sum(values)/2.0
        self.dp = [None for i in xrange(len(values)+1)]
        
        self.dp[0] = 0
        self.dp[1] = values[-1]
        self.dp[2] = max(values[-1], values[-1]+values[1-2])
        
        
        return self.compute(len(values), values) > target
        
    def compute(self, n, values):
        if n < 0:
            return 0
            
        if self.dp[n] is not None:
            return self.dp[n]
            
        pickOne = min(self.compute(n-2, values), self.compute(n-3, values))+values[-n]
        pickTwo = min(self.compute(n-3, values), self.compute(n-4, values))+values[-n] + values[-n+1]
        # print pickOne, pickTwo
        self.dp[n] = max(pickOne, pickTwo)
        return self.dp[n]
        
        
        