# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/continuous-subarray-sum-ii
@Language: Python
@Datetime: 16-10-12 23:37
'''

class Solution:
    # @param {int[]} A an integer array
    # @return {int[]} A list of integers includes the index of the 
    # first number and the index of the last number
    def continuousSubarraySumII(self, A):
        # Write your code here
        if A is None or len(A) == 0:
            return None
        
        l = len(A)
        cmax, cmin = A[0], A[0]
        maxsum, minsum = 0, 1
        max_start, min_start = 0, 0
        max_res, min_res = [0,0], [0, 0]
        asum = 0
        
        for i in xrange(l):
            asum += A[i]
            
            # find continous max
            if maxsum < 0:
                maxsum = A[i]
                max_start = i
            else:
                maxsum += A[i]
            
            if maxsum > cmax:
                cmax = maxsum
                max_res = [max_start, i]
                
            # find continous min
            if minsum > 0:
                minsum = A[i]
                min_start = i
            else:
                minsum += A[i]
            
            if minsum < cmin:
                cmin = minsum
                min_res = [min_start, i]
        
        # print asum, cmax, max_res, cmin, min_res
        if cmax >= asum - cmin or asum == cmin:
            return max_res
        else:
            tail, head = min_res[0]-1, min_res[1]+1
            if head > l-1:
                head = 0
            
            if tail < 0:
                tail = l - 1
            
            return [head, tail]
                
            
        