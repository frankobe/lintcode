# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/unique-paths
@Language: Python
@Datetime: 15-07-27 06:39
'''

class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    
    def uniquePaths(self, m, n):
        # write your code here
        
        if m == 0 or n == 0:
            return 0
        
        f = [[None for i in range(n)] for j in range(m)]
        
        for i in range(m):
            f[i][0] = 1
            
        for j in range(n):
            f[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                f[i][j] = f[i-1][j] + f[i][j-1]
        
        return f[m-1][n-1]