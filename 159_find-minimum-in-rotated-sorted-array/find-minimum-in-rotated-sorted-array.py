# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array
@Language: Python
@Datetime: 16-02-04 19:13
'''

class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if num is None or len(num) == 0:
            return None
        
        start, end = 0, len(num)-1
        while start + 1 < end:
            mid = (start + end)/2
            
            if num[start] > num[mid]:
                end = mid
            
            elif num[end] < num[mid]:
                start = mid
            
            else:
                # no pivot
                return num[start]
        
        return min(num[start], num[end])
            