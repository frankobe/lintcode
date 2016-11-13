# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/burst-balloons
@Language: Python
@Datetime: 16-04-27 06:36
'''

class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return {int} an integer, maximum coins
    """
    def maxCoins(self, nums):
        # Write your code here
        if nums is None or len(nums) == 0:
            return 0
            
        n = len(nums)
        self.dp = [[None for i in xrange(n+2)] for j in xrange(n+2)]
        self.dummyNums = [None]*(n+2)
        for i in xrange(n):
            self.dummyNums[i+1] = nums[i]
        
        self.dummyNums[0] = 1
        self.dummyNums[n+1] = 1
            
        
        return self.compute(1, n)
        
    def compute(self, i, j):
            
        if self.dp[i][j] is not None:
            return self.dp[i][j]
        
        lastVal= 0
        for k in xrange(i, j+1):
            lastVal = max(self.dummyNums[i-1]*self.dummyNums[k]*self.dummyNums[j+1] + self.compute(i, k-1) \
                        + self.compute(k+1, j), lastVal)
                        
        self.dp[i][j] = lastVal
        return lastVal