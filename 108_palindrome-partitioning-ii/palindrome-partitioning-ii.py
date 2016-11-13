# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/palindrome-partitioning-ii
@Language: Python
@Datetime: 15-09-08 14:48
'''

class Solution:
    # @param s, a string
    # @return an integer
    
    def isPalindrome(self, s):
        if s is None or len(s) == 0:
            return True
        
        l = len(s)
        
        if l == 1:
            return True
            
        for i in range(l/2):
            if s[i] != s[-i-1]:
                return False
                
        return True
        
    def calAllPalindrome(self, s):
        if s is None or len(s) == 0:
            return -1
            
        l = len(s)
        f = [[False for i in range(l)] for j in range(l)]
        
        # attention
        for i in range(l):
            f[i][i] = True
            
        for i in range(l-1):
            f[i][i+1] = s[i] == s[i+1]
            
        for length in range(2, l):
            for i in range(0, l-length):
                f[i][i+length] = f[i+1][i+length-1] and s[i] == s[i+length]
            
        return f
        
    def minCut(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return 0
            
        l = len(s)
        f = [i for i in range(l)]
        checkT = self.calAllPalindrome(s)
        
        for i in range(l):
            for j in range(i+1):
                if checkT[j][i]:
                    if j == 0:
                        f[i] = 0
                        break
                    else:
                        f[i] = min(f[j-1] + 1, f[i])
                    
        return f[l-1]
                
                
        
