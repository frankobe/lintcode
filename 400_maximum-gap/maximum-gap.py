# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/maximum-gap
@Language: Python
@Datetime: 16-10-15 00:14
'''

import math
class Solution:
    # @param nums: a list of integers
    # @return: the maximum difference
    def maximumGap(self, nums):
        # write your code here
        if nums is None or len(nums) < 2:
            return 0
        n = len(nums)
        if n == 2:
            return abs(nums[0]-nums[1])
        # linear sorting algorithm
        kmax, kmin = max(nums), min(nums)
        
        if kmax == kmin:
            return 0
        
        
        bucketSize = (kmax - kmin+1)/(n-1)
        if bucketSize == 0:
            bucketSize = 1
        
        localMin = [sys.maxint]*n
        localMax = [-1]*n
        
        for i in nums:
            t = (i - kmin+1)/bucketSize-1
            localMin[t] = min(localMin[t], i)
            localMax[t] = max(localMax[t], i)
        
        maxGap = 0
        lastMax = 0
        for i in xrange(n):
            if localMax[i] != -1 and localMin[i] != -1:
                if i == 0:
                    maxGap = localMax[i] - localMin[i]
                else:
                    maxGap = max(localMin[i] - lastMax, localMax[i] - localMin[i], maxGap)
                    
                lastMax = localMax[i]
        
        return maxGap
            
        
        return maxGap