# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/wiggle-sort-ii
@Language: Python
@Datetime: 16-10-18 23:38
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
        mid = self.findNthLargest(0, n/2, n-1, nums)
        order = range(1, n, 2)+range(0, n, 2)
        left, right, current = 0, n-1, 0
        while current <= right:
            if nums[order[current]] > mid:
                nums[order[current]], nums[order[left]] = nums[order[left]], nums[order[current]]
                current += 1
                left += 1
            elif nums[order[current]] < mid:
                nums[order[current]], nums[order[right]] = nums[order[right]], nums[order[current]]
                right-=1
            else:
                current+=1

        return nums
        
    def findNthLargest(self, start, nth, end, array):
        pivot = array[start]
        left, right = start, end
        while left < right:
            while left < right and array[right] >= pivot:
                right -= 1

            array[left], array[right] = array[right], array[left]

            while left < right and array[left] <= pivot:
                left += 1

            array[left], array[right] = array[right], array[left]
        if left - start == nth:
            return pivot
        elif left-start < nth:
            return self.findNthLargest(left+1, nth - (left-start+1), end, array)
        else:
            return self.findNthLargest(start, nth, right-1, array)
    
    #magic rewire func 

    def rewire(self, i, n):
        return (1+2*i)%(n|1)