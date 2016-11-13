# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/jump-game
@Language: Python
@Datetime: 15-07-27 18:30
'''

class Solution:
    # @param A, a list of integers
    # @return a boolean

    def canJump(self, A):
        # write your code here
        if A is None:
            return False
            
        m = len(A)
        f = [False for i in range(m)]
        f[0] = True
        
        for i in range(m):
            if f[i]:
                for j in range(1, min(A[i], m - i)):
                    f[i+j] = True
                    
        return f[m-1]
        
        
            
