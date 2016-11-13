# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/search-in-rotated-sorted-array-ii
@Language: Python
@Datetime: 16-02-05 07:10
'''

class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        # write your code here
        if A is None or len(A)==0 or target is None:
            return False
            
        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = (start+end)/2
                
            if A[start] > A[mid]:
                if A[mid] < target and target < A[end]:
                    start = mid
                else:
                    end = mid
            elif A[start] > A[mid]:
                if A[start] <= target and target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:    
                if A[start] == target:
                    return True
                else:
                    start = start + 1
                    
        if A[start] == target:
            return True
        
        if A[end] == target:
            return True
        
        return False