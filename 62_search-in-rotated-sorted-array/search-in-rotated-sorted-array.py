# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/search-in-rotated-sorted-array
@Language: Python
@Datetime: 16-10-25 19:48
'''

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return -1
        
        start, end = 0, len(A)-1
        
        while start + 1 < end:
            mid = start+(end-start)/2
            
            if A[start] > A[mid]:
                if A[mid] <= target and target <= A[end]:
                    start = mid
                else:
                    end = mid
            else:
                if target <= A[mid] and target >= A[start]:
                    end = mid
                else:
                    start = mid
                
        if A[start] == target:
            return start
        
        if A[end] == target:
            return end
        
        return -1
            
        
                
        
        
        