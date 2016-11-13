# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/search-insert-position
@Language: Python
@Datetime: 16-01-31 05:28
'''

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    # def searchInsert(self, A, target):
    #     # write your code here
    #     if A is None or len(A) == 0 or target is None:
    #         return 0
           
    #     start, end = 0, len(A) - 1
        
    #     while start + 1 < end:
            
    #         mid = (start + end)/2
            
    #         if A[mid] > target:
    #             end = mid
                
    #         else:
    #             start = mid
                
    #     if A[start] >= target:
    #         return start 
            
    #     if A[start] < target and A[end] >= target:
    #         return end
            
    #     if A[end] < target:
    #         return end + 1
    
    def searchInsert(self, A, target):
        if A is None or len(A) == 0 or target is None:
            return 0
        
        start, end = 0, len(A) - 1
        
        while start < end:
            if start + 1 == end:
                break
            
            mid = (start + end)/2
            
            if A[mid] >= target:
                end = mid
            else:
                start = mid
                
        if A[start] >= target:
            return start
            
        elif A[end] >= target:
            return end
        else:
            return end+1
            
            
            