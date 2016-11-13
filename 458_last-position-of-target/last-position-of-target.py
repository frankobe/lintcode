# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/last-position-of-target
@Language: Python
@Datetime: 16-02-03 07:34
'''

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def lastPosition(self, A, target):
        # Write your code here
        if A is None or len(A) == 0 or target is None:
            return -1
            
        start, end = 0, len(A) - 1
        
        while start < end:
            mid = (start+end)/2
            
            if mid == start:
                break
            
            if A[mid] > target:
                end = mid
            else:
                start = mid
                
        if A[end] == target:
            return end
        elif A[start] == target:
            return start
        else:
            return -1