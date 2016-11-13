# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/subarray-sum-closest
@Language: Python
@Datetime: 16-10-13 00:59
'''

import math
class Solution:
 """
 @param nums: A list of integers
 @return: A list of integers includes the index of the first number 
 and the index of the last number
 """
 def subarraySumClosest(self, nums):
    # write your code here
    if nums is None or len(nums) == 0:
        return None
    # [trick]
    if len(nums) == 1:
        return [0, 0]
        
    l = len(nums)
    f = [(nums[0], 0) for i in xrange(l)]
    
    for i in xrange(1, l):
        f[i] = (f[i-1][0]+nums[i], i)
    
    # nlog(n) can be sorting
    f = sorted(f) 
    # print f
    minDiff = abs(f[0][0])
    start, end = 0, 0 
    for i in xrange(1, l):
        if f[i][0] - f[i-1][0] < minDiff:
            minDiff = f[i][0] - f[i-1][0]
            start = min(f[i][1], f[i-1][1])+1
            end = max(f[i][1], f[i-1][1])
    
    return [start, end]
            
        
        
            
            
    
        