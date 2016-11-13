# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/scramble-string
@Language: Python
@Datetime: 16-04-27 18:09
'''

class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):
        # Write your code here
        
        if s1 is None and s2 is None:
            return True
        
        if s1 is None or s2 is None:
            return False
        
        n, m = len(s1), len(s2)
        if n != m:
            return False
            
        # init 
        self.dp = [[[None for i in xrange(n+1)] for j in xrange(n)] \
                    for k in xrange(n)]
                    
        return self.compute(0, 0, n, s1, s2)
        
    def compute(self, i1, i2, l, s1, s2):
        if self.dp[i1][i2][l] is not None:
            return self.dp[i1][i2][l]
        
        if l == 1:
            self.dp[i1][i2][l] = s1[i1] == s2[i2]
            return self.dp[i1][i2][l]
            
        res = False
        for k in xrange(1, l):
            res = (self.compute(i1, i2, k, s1, s2) and self.compute(i1+k, i2+k, l-k ,s1, s2)) \
                or (self.compute(i1+k, i2, l-k, s1, s2) and self.compute(i1, i2+l-k, k, s1, s2))
                
            if res:
                break
            
        self.dp[i1][i2][l] = res
        return res
        
        # stat func: start from s1[x], s2[y], next k character is scrambled
        # dp[x][y][k] = (dp[x][y][i] and dp[x+i][y+i][k-i]) 
        #           or (dp[x+i][y][k-i] and dp[x][y+k-i][i])
        
        
        
        