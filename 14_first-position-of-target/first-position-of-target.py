# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/first-position-of-target
@Language: Python
@Datetime: 15-06-24 17:35
'''

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0 or target is None:
            return -1
        
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end)/2
            
            if target <= nums[mid]:
                end = mid 
            else:
                start = mid
                
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1