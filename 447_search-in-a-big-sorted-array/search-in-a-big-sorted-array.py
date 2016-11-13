# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/search-in-a-big-sorted-array
@Language: Python
@Datetime: 15-10-05 00:22
'''

class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @return {int} an integer
    
    def searchHelper(self, A, target, start, end):
        if start > end:
            return -1
            
        if start == end:
            if target == A[start]:
                return start
            else:
                return -1
                
        half = (start + end)/2
        
        if A[half] >= target:
            return self.searchHelper(A, target, start, half)
        else:
            return self.searchHelper(A, target, half+1, end)


            
    def searchBigSortedArray(self, A, target):
        # write your code here
        if target is None or A is None or len(A) == 0:
            return -1
        
        end  = 0
        while end < len(A) and A[end] < target:
            end = end * 2 + 1
            
        end = min(end, len(A)-1)    
        
        return self.searchHelper(A, target, 0, end)