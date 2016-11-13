# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/climbing-stairs
@Language: Python
@Datetime: 15-07-27 07:15
'''

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
            
        if n == 1:
            return 1
        
        f = [0 for i in range(n)] 
        f[0] = 1
        f[1] = 2
        
        for i in range(2, n):
            f[i] = f[i-1] + f[i-2]
        
        return f[n-1]

