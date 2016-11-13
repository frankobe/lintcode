# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/wiggle-sort
@Language: Python
@Datetime: 16-10-17 18:31
'''

class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        # Write your code here
        if nums is None or len(nums) == 0:
            return None
            
        n = len(nums)
        for i in xrange(1, n):
            if i%2 == 1 and nums[i] < nums[i-1] or \
                i%2 == 0 and nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]   
    
        return nums
            