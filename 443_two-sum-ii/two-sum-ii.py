# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/two-sum-ii
@Language: Python
@Datetime: 16-04-04 03:52
'''

class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer
    def twoSum2(self, nums, target):
        # Write your code here
        if nums is None or len(nums) == 0:
            return 0
            
        start, end = 0, len(nums) - 1
        count = 0 
        
        nums.sort()
        
        while start < end:
            if nums[start] + nums[end] > target:
                count += end - start
                end -= 1
            else:
                start += 1
        
        return count
        