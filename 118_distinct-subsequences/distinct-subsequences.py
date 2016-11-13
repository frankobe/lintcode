# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/distinct-subsequences
@Language: Python
@Datetime: 15-08-18 23:51
'''

class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
        
        l_s, l_t = len(S), len(T) 
        
        if l_s == 0:
            return 0
        
        if l_t == 0:
            return 1
            
        list = [[0 for j in xrange(l_t+1)] for i in xrange(l_s+1)]
        
        for j in xrange(l_t+1):
            list[0][j] = 0
            
        for i in xrange(l_s+1):
            list[i][0] = 1
            
        for i in xrange(1, l_s+1):
            for j in xrange(1, l_t+1):
                if i < j:
                    list[i][j] = 0
                else:
                    if S[i-1] == T[j-1]:
                        list[i][j] = list[i-1][j-1] + list[i-1][j]
                    else:
                        list[i][j] = list[i-1][j]
                        
        
        return list[l_s][l_t]