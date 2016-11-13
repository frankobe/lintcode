# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/longest-common-substring
@Language: Python
@Datetime: 16-02-23 21:43
'''

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    # def longestCommonSubstring(self, A, B):
    #     # write your code here
        
    #     if len(A) == 0 or len(B) == 0:
    #         return 0
            
    #     l_a = len(A)
    #     l_b = len(B)
    #     maxLen = 0
        
    #     f = [[0 for i in xrange(l_b+1)] for j in xrange(l_a+1)]
        
    #     for i in xrange(l_a):
    #         for j in xrange(l_b):
    #             if A[i] == B[j]:
    #                 f[i+1][j+1] = f[i][j] + 1
    #                 maxLen = max(f[i+1][j+1], maxLen)
                    
    #     return maxLen
        
    def longestCommonSubstring(self, A, B):
        # write your code here
        
        if A is None or len(A) == 0 or B is None and len(B) == 0:
            return 0
        
        l_a = len(A)
        l_b = len(B)
        maxLen = 0
        
        f = [[0 for i in xrange(l_b+1)] for j in xrange(l_a+1)]
        
        for i in xrange(l_a):
            for j in xrange(l_b):
                if A[i] == B[j]:
                    f[i+1][j+1] = f[i][j] + 1
                    maxLen = max(f[i+1][j+1], maxLen)
                    
        return maxLen
                
