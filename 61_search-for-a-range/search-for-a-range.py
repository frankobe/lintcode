# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/search-for-a-range
@Language: Python
@Datetime: 15-06-24 18:06
'''

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if A is None or len(A) == 0 or target is None:
            return [-1, -1]
            
        start, end = 0, len(A) - 1
        leftBound, rightBound = -1, -1
        
        while start + 1 < end:

            mid = (start + end) / 2
            
            if A[mid] <= target:
                start = mid
            
            if A[mid] > target:
                end = mid
                
        if A[start] ==  target:
            rightBound = start
            
        if A[end] == target:
            rightBound = end
            
        if rightBound != -1:
            start, end = 0, rightBound
            
            while start + 1 < end:

                mid = (start + end) / 2
            
                if A[mid] < target:
                    start = mid
            
                if A[mid] >= target:
                    end = mid
             
            if A[end] == target:
                leftBound = end  
            
            if A[start] == target:
                leftBound = start
            

        
        return [leftBound, rightBound]
        