# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/backpack-iv
@Language: Python
@Datetime: 16-11-03 18:56
'''

class Solution:
    # @param {int[]} nums an integer array and all positive numbers, no duplicates
    # @param {int} target an integer
    # @return {int} an integer
    def backPackIV(self, nums, target):
        # Write your code here
        if not nums or target < 0:
            return 0
            
        # dp[i][j] = dp[i-1][j] + dp[i][j-A[i-1]])
        n = len(nums)
        dp = [[0 for i in xrange(target+1)] for j in xrange(n+1)]
        
        for i in xrange(n+1):
            dp[i][0] = 1
            
        for i in xrange(1, n+1):
            for j in xrange(1, target+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][target]