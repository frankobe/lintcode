# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/minimum-path-sum
@Language: Python
@Datetime: 15-07-02 19:23
'''

class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if grid is None or len(grid) == 0:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # state function, f[x][y] for min sum from (0,0) to (x,y)
        # f[x][y] = min(f[x-1][y], f[x][y-1]) + grid[x][y]
        
        # init
        f = [[None for i in range(n)] for j in range(m)] 
        f[0][0] = grid[0][0]
        
        for i in range(1, m):
            f[i][0] = f[i-1][0] + grid[i][0]
            
        for j in range(1, n):
            f[0][j] = f[0][j-1] + grid[0][j]
            
        for i in range(1,m):
            for j in range(1,n):
                f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]
                
        return f[m-1][n-1]
        