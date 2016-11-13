# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/classical-binary-search
@Language: Python
@Datetime: 16-02-03 07:43
'''

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        # Write your code here
        if A is None or len(A) == 0 or target is None:
            return -1
            
        if len(A) == 1:
            if A[0] == target:
                return 0
            else:
                return -1
        else:
            return self.iterator(A, target, 0, len(A) - 1)
    
    def iterator(self, A, target, start, end):
        if start + 1 == end:
            if A[start] == target:
                return start
            elif A[end] == target:
                return end
            else:
                return -1
        else:
            mid = (start+end)/2
            if A[mid] == target:
                return mid
            
            if A[mid] > target:
                return self.iterator(A, target, start, mid)
            else:
                return self.iterator(A, target, mid, end)