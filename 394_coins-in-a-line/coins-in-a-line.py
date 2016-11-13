# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/coins-in-a-line
@Language: Python
@Datetime: 16-04-24 07:49
'''

class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        if n < 1:
            return False
        
        self.dp = {}
        self.dp[0] = False
        self.dp[1] = True
        self.dp[2] = True
        
        return self.compute(n)
        
    def compute(self, n):
        if n in self.dp:
            return self.dp[n]
        else:
            self.dp[n] = (self.compute(n-2) and self.compute(n-3)) \
                    or  (self.compute(n-3) and self.compute(n-4))
        
        return self.dp[n]