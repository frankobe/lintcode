# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/minimum-size-subarray-sum
@Language: Python
@Datetime: 16-05-03 07:17
'''

class Solution:
     # @param nums: a list of integers
     # @param s: an integer
     # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        
        n = len(nums)
        left, right = 0, 0
        tmpSum = 0
        minLen = n+1
        while right < n:
            while right < n and tmpSum < s:
                tmpSum += nums[right]
                right += 1
            if tmpSum < s: 
                break
            while left < right and tmpSum >= s:
                tmpSum -= nums[left]
                left += 1
            
            minLen = min(minLen, right - left+1)
            
        return -1 if minLen == n+1 else minLen
                
            
            
        
        
            