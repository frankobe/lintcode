# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/closest-number-in-sorted-array
@Language: Python
@Datetime: 16-02-03 05:49
'''

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def closestNumber(self, A, target):
        # Write your code here
        if A is None or len(A) == 0 or target is None:
            return -1
            
        start, end = 0, len(A) -1 
        
        while start < end:
            mid = (start+end)/2
            
            if mid == start:
                break
            
            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                return mid
        
        if target - A[start] > A[end] - target:
            return end
        else:
            return start