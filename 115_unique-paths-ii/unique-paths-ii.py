# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/unique-paths-ii
@Language: Python
@Datetime: 15-07-27 07:05
'''

class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here

        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0 or obstacleGrid is None:
            return 0
            
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        f = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                f[i][0] = 1
            else:
                break
        
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                f[0][j] = 1
            else:
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    f[i][j] = f[i-1][j] + f[i][j-1]
                    
                else:
                    f[i][j] = 0
                    
        return f[m-1][n-1]
        