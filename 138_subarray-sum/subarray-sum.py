# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/subarray-sum
@Language: Python
@Datetime: 16-02-16 19:55
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return None
            
        if len(nums) == 1 and nums[0] == 0:
            return [0, 0]
        
        dic = {}
        sum = 0
        for i in xrange(len(nums)):
            sum = sum + nums[i]
            if sum == 0:
                return [0, i]
                
            if sum in dic:
                return [dic[sum]+1, i]
            else:
                dic[sum] = i
        return None