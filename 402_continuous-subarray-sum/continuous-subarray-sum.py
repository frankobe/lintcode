# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/continuous-subarray-sum
@Language: Python
@Datetime: 16-10-12 22:55
'''

class Solution:
 # @param {int[]} A an integer array
 # @return {int[]} A list of integers includes the index of the 
 # first number and the index of the last number
 def continuousSubarraySum(self, A):
    # Write your code here
    if A is None or len(A) == 0:
        return None
    l = len(A)
    
    sum = 0
    maxVal = A[0]
    start, end = 0, 0
    res = [0, 0]
    for i in xrange(l):
        if sum < 0:
            sum = A[i]
            start = i
        else:
            sum += A[i]
        
        if sum > maxVal:
            maxVal = sum
            res = [start, i]
                
    return res