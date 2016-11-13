# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/total-occurrence-of-target
@Language: Python
@Datetime: 16-02-02 07:35
'''

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def totalOccurrence(self, A, target):
        # Write your code here
        if A is None or len(A) == 0 or target is None:
            return 0
        
        if len(A) == 1:
            if A[0] == target:
                return 1
            else:
                return 0
                
        least = self.findLeast(target, 0, len(A) - 1, A)
        largest = self.findLargest(target, 0, len(A) - 1, A)
        if least == -1 or largest == -1:
            return 0
        else:
            return largest - least + 1
        
    def findLeast(self, target, start, end, A):
        if start + 1 == end:
            if A[start] == target:
                return start
            elif A[end] == target:
                return end
            else:
                return -1
        else:
            mid = (start+end)/2
            if A[mid] > target:
                end = mid
            elif A[mid] == target:
                end = mid
            else:
                start = mid
            
            return self.findLeast(target, start, end, A)
 
    def findLargest(self, target, start, end, A):
        if start + 1 == end:
            if A[end] == target:
                return end
            elif A[start] == target:
                return start
            else:
                return -1
        else:
            mid = (start+end)/2
            if A[mid] > target:
                end = mid
            elif A[mid] == target:
                start = mid
            else:
                start = mid
            
            return self.findLargest(target, start, end, A)               
        
            
        
        