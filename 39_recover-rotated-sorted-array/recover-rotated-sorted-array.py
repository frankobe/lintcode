# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/recover-rotated-sorted-array
@Language: Python
@Datetime: 15-06-29 07:19
'''

class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray1(self, nums):
        # write your code here
        
        if len(nums) == 0 or nums is None:
            return
        
        index = -1
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i+1]:
                index = i
                break
            else:
                continue
        
        if index != -1:
            nums.extend(nums[0:index+1])
            for i in range(0, index+1):
                nums.remove(nums[0])
    
    # 2
    def reverse(self, array):
        for i in range(0, len(array)/2):
           array[i] = array[-(i+1)] + array[i]
           array[-(i+1)] = array[i] - array[-(i+1)]
           array[i] = array[i] - array[-(i+1)]
           
        return array
        
    def recoverRotatedSortedArray(self, nums):
        
        if len(nums) == 0 or nums is None:
            return
        
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[0:i+1] = self.reverse(nums[0:i+1])
                nums[i+1:] = self.reverse(nums[i+1:])
                nums = self.reverse(nums)

    
            
            