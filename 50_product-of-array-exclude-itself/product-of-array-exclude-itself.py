# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/product-of-array-exclude-itself
@Language: Python
@Datetime: 16-02-28 10:24
'''

class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        
        if A is None or len(A) == 0:
            return []
        
        result = []
        for i in xrange(len(A)):
            result.append(self.B(A, i))
            
        return result
        
    def B(self, A, i):
        b = 1
        for x in xrange(len(A)):
            if x != i:
                b *= A[x]
                
        return b
            