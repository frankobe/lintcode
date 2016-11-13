# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/interleaving-string
@Language: Python
@Datetime: 15-08-19 01:27
'''

class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l3 != l1+l2:
            return False
            
        if l1 == 0:
            return s2 == s3
        
        if l2 == 0:
            return s1 == s3
        
        f = [[False for j in xrange(l2+1)] for i in xrange(l1+1)]
            
        for i in xrange(l1):
            f[i+1][0] = s3[:i+1] == s1[:i+1]
        
        for j in xrange(l2):
            f[0][j+1] = s3[:j+1] == s2[:j+1]
            
        f[0][0] = True
        
        for i in xrange(1, l1+1):
            for j in xrange(1, l2+1):
                f[i][j] = (f[i-1][j] and s1[i-1] == s3[i+j-1]) or (f[i][j-1] and s2[j-1] == s3[i+j-1])
                
        return f[l1][l2]
        
        