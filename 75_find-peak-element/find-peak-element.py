# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/find-peak-element
@Language: Python
@Datetime: 15-06-29 07:52
'''

class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    
    def findPeak(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return -1
            
        start, end = 1, len(A) - 2
        
        while start + 1 < end:
            mid = (start + end)/2
            
            if A[mid] > A[mid -1] and A[mid] > A[mid + 1]:
                return mid
                
            if A[mid] < A[mid - 1]:
                end = mid
            else:
                start = mid
                
        
        if A[start] < A[end]:
            return end
            
        else:
            return start
            
            
            
        
            