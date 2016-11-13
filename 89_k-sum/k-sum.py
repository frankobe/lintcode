# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/k-sum
@Language: Python
@Datetime: 15-10-13 16:29
'''

class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        # write your code here
        if A is None or k < 0 or target < 0:
            return 0
        
        if k == 0 and target == 0:
            return 1
        
        ans = [[[0 for l in range(target + 1)] for m in range(k + 1)] for n in range(len(A) + 1)]
        
        # init
        for l in xrange(len(A)+1):
            ans[l][0][0] = 1
        
        for l in xrange(1, len(A)+1):
            item  = A[l-1]
            for m in xrange(1, target + 1):
                for n in range(1, min(k+1, l+1)):
                    if m >= item:
                        ans[l][n][m] += ans[l-1][n-1][m-item]
                    
                    ans[l][n][m] += ans[l-1][n][m]    
        return ans[len(A)][k][target]

        
        