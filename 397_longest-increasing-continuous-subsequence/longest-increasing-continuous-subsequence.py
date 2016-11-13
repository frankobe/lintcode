# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/longest-increasing-continuous-subsequence
@Language: Python
@Datetime: 16-04-24 01:59
'''

class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        if A is None or len(A) == 0:
            return 0
            
        num = [(1, 0)]
        maxCount = 1
        for i in xrange(1, len(A)):
            if A[i] > A[i-1]:
                if num[i-1][1] >= 0:
                    num.append((num[i-1][0]+1,1))
                else:
                    num.append((2,1))
            else:
                if num[i-1][1] <= 0:
                    num.append((num[i-1][0]+1, -1))
                else:
                    num.append((2,-1))
                    
            maxCount = max(maxCount, num[i][0])
            
        return maxCount
                    
            
            
                
                
            
            