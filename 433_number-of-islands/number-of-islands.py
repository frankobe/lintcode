# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/number-of-islands
@Language: Python
@Datetime: 16-03-27 23:23
'''

class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        m = len(grid)
        if m == 0:
            return 0
        
        n = len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
        
        def check(x,y):
            if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == 1 and visited[x][y] == False:
                return True
            return False
        
        def dfs(x, y):
            nRow = [-1, 0, 1, 0]
            nCol = [0, -1, 0, 1]
            for i in xrange(4):
                nextX = x + nRow[i]
                nextY = y + nCol[i]
                if check(nextX, nextY):
                    visited[nextX][nextY] = True 
                    dfs(nextX,nextY)
                    
        count = 0
        for x in xrange(m):
            for y in xrange(n):
                if check(x, y):
                    visited[x][y] = True
                    dfs(x, y)
                    count += 1
                
        return count
                
        
        
        