# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/longest-common-subsequence
@Language: Python
@Datetime: 15-08-03 23:14
'''

class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        if len(A) == 0 or len(B) == 0:
            return 0
            
        l_a = len(A)
        l_b = len(B)
        
        f = [[0 for i in xrange(l_b+1)] for j in xrange(l_a+1)]
        
        for i in xrange(l_a):
            for j in xrange(l_b):
                if A[i] == B[j]:
                    f[i+1][j+1] = f[i][j] + 1
                else:
                    f[i+1][j+1] = max(f[i][j+1], f[i+1][j])
        
        return f[-1][-1]
