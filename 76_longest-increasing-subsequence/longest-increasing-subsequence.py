# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/longest-increasing-subsequence
@Language: Python
@Datetime: 15-08-03 05:13
'''

class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
        
        l = len(nums)
        f = [1 for i in range(l)]
        
        for i in xrange(1,l):
            for j in xrange(i-1, -1, -1):
                if nums[i] >= nums[j]:
                    f[i] = max(f[i], f[j]+1)
        return max(f)
