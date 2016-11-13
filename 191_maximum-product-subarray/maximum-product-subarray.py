# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/maximum-product-subarray
@Language: Python
@Datetime: 16-07-05 17:54
'''

class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
            
        f = [nums[0]]
        g = [nums[0]]
        
        for i in xrange(1, len(nums)):
            f.append(max(f[i-1]*nums[i], g[i-1]*nums[i], nums[i]))
            g.append(min(f[i-1]*nums[i], g[i-1]*nums[i], nums[i]))
            
        return max(f)
        
        