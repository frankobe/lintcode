# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/backpack-vi
@Language: Python
@Datetime: 16-11-03 22:26
'''

class Solution:
    # @param {int[]} nums an integer array and all positive numbers, no duplicates
    # @param {int} target an integer
    # @return {int} an integer
    def backPackVI(self, nums, target):
        # Write your code here
        if not nums and target < 0:
            return 0
            
        dp = [0 for i in xrange(target+1)]
        dp[0] = 1
        
        for i in xrange(1, target+1):
            for item in nums:
                if i >= item:
                    dp[i] += dp[i-item]
                    
        return dp[target]