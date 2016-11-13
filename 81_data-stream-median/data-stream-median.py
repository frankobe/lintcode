# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/data-stream-median
@Language: Python
@Datetime: 16-04-22 18:10
'''

class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianII(self, nums):
        # write your code here
        
        sortList = []
        result = []
        for i in xrange(len(nums)):
            self.binaryInsert(sortList, nums[i])
            # print sortList
            result.append(sortList[i/2])

        return result
    
    def binaryInsert(self, nums, val):
        start, end = 0, len(nums)-1
        if len(nums) == 0:
            nums.insert(0, val)
            return

        while start < end:
            if start + 1 == end:
                if val <= nums[start]:
                    nums.insert(start, val)
                elif val < nums[end]:
                    nums.insert(end,val)
                else:
                    nums.insert(end+1, val)
                return

            mid = (start+end)/2

            if val > nums[mid]:
                start = mid+1
            elif val < nums[mid]:
                end = mid-1
            else:
                nums.insert(mid, val)
                return

        if start == end:
            if nums[start] > val:
                nums.insert(start, val)
            else:
                nums.insert(start+1, val)
        