# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/sort-colors
@Language: Python
@Datetime: 16-03-30 06:12
'''

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return []
        # sol 1: 2 pointers
        # n = len(nums)
        # pl, pr = 0, n-1
        # i = 0
        
        # def swap(i, j):
        #     tmp = nums[i]
        #     nums[i] = nums[j]
        #     nums[j] = tmp
        
        # while i <= pr:
        #     if nums[i] == 0:
        #         swap(pl, i)
        #         pl += 1
        #         i += 1
        #     elif nums[i] == 1:
        #         i += 1
        #     else:
        #         swap(pr, i)
        #         pr -= 1
        
        # sol 2
        self.sortHelper(nums, 1, self.sortHelper(nums, 0, 0))
        
    def sortHelper(self, a, target, head):
        start, end = head, len(a) - 1
        while start <= end:
            while start <= end and a[start] == target:
                start += 1
            
            while start <= end and a[end] != target:
                end -= 1
                
            if start <= end:
                a[start], a[end] = a[end], a[start]
                start += 1
                end -= 1
        return start
    
        
        
            