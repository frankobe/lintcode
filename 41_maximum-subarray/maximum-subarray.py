# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/maximum-subarray
@Language: Python
@Datetime: 16-02-23 21:48
'''

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
            
        # DP
        # sum, maxSum, minSum = 0, -sys.maxint-1, 0
        # for i in xrange(len(nums)):
        #     sum = sum + nums[i]
        #     maxSum = max(maxSum, sum - minSum)
        #     minSum = min(minSum, sum)
            
        # return maxSum
        
        #Greedy
        sum, maxSum = 0, -sys.maxint - 1
        for i in xrange(len(nums)):
            sum = sum + nums[i]
            maxSum = max(maxSum, sum)
            sum = max(sum, 0)
            
        return maxSum
            