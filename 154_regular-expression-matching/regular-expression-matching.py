# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/regular-expression-matching
@Language: Python
@Datetime: 16-09-28 01:21
'''

class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    
    def isMatch(self, s, p):
        # write your code here
        # dp
        if p is None or len(p) == 0:
            return False
        
        sl, pl = len(s), len(p)
        
        dp = [[False for i in xrange(pl+1)] for j in xrange(sl+1)]
        
        dp[0][0] = True
        
        for i in xrange(1, pl+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
                
        for i in xrange(1, sl+1):
            for j in xrange(1, pl+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (self.isSame(s[i-1], p[j-2]) and dp[i-1][j])
                elif self.isSame(s[i-1], p[j-1]):
                    dp[i][j] = dp[i-1][j-1]
            
        return dp[sl][pl]
        
    # def isMatch(self, s, p):
    #     # write your code here
        
    #     if p is None or len(p) == 0:
    #         return False
        
    #     sl, pl = len(s), len(p)
        
    #     mem = [[-1 for i in xrange(pl+1)] for j in xrange(sl+1)]
    #     return self.dfsmem(s, p, 0, 0, mem)
        
        
    # def dfsmem(self,s, p, si, pi, mem):
    #     sl, pl = len(s), len(p)
    #     if pi >= pl:
    #         return si >= sl
    
    #     if mem[si][pi] != -1:
    #         return True if mem[si][pi] == 1 else False
    
    #     if pi != pl -1 and p[pi+1] == '*':
    #         # 1.1 skip pi
    #         if self.dfsmem(s, p, si, pi+2, mem):
    #             mem[si][pi+2] = 1
    #             return True
    #         else:
    #             mem[si][pi+2] = 0
    
    #         for i in xrange(si, sl):
    #             if not self.isSame(s[i], p[pi]):
    #                 return False
    
    #             if self.dfsmem(s, p, i+1, pi+2, mem):
    #                 mem[i+1][pi+2] = 1
    #                 return True
    #             else:
    #                 mem[i+1][pi+2] = 0
    
    #         return False
    
    #     else:
    #         if si >= sl:
    #             return False
    
    #         if not self.isSame(s[si], p[pi]):
    #             return False
    
    #         mem[si+1][pi+1] = self.dfsmem(s, p, si+1, pi+1, mem)        
    #         return mem[si+1][pi+1]
    

    def isSame(self, c, p):
        return p == '.' or c == p