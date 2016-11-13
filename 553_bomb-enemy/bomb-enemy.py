# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/bomb-enemy
@Language: Python
@Datetime: 16-11-07 17:34
'''

class Solution:
    # @param {character[][]} grid Given a 2D grid, each cell is either 'W', 'E' or '0'
    # @return {int} an integer, the maximum enemies you can kill using one bomb
    def maxKilledEnemies(self, grid):
        # Write your code here
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])    
    #1.bfs: MLE and TLE        
        # e_list = []
        # for i in xrange(m):
        #     for j in xrange(n):
        #         if grid[i][j] == 'E':
        #             e_list.append((i, j))
        
        # l = len(e_list)

    #     reachable = [[0 for i in xrange(n)] for j in xrange(m)]
                    
    #     for k in xrange(l):
    #         self.bfs(e_list[k], reachable, grid)
            
    #     maxcount = 0
    #     for i in xrange(m):
    #         for j in xrange(n):
    #             if grid[i][j] == '0':
    #                 maxcount = max(reachable[i][j], maxcount)
                    
    #                 if maxcount == l:
    #                     return l
    #     return maxcount
        
    # def bfs(self, enemy, reach, grid):
    #     m, n = len(grid), len(grid[0])
    #     d_x = [-1, 0, 0, 1]
    #     d_y = [0, -1, 1, 0]
    #     (x, y) = enemy
    #     for i in xrange(4):
    #         n_x = d_x[i]+x
    #         n_y = d_y[i]+y
    #         while self.isValid(n_x, n_y, m, n) and grid[n_x][n_y] != 'W' :
    #             reach[n_x][n_y] += 1
    #             n_x += d_x[i]
    #             n_y += d_y[i]
                        
    # def isValid(self, x, y, m ,n):
    #     if x >=0 and x < m and y >= 0 and y < n:
    #         return True
    #     else:
    #         return False
    
    
    # 2. count enemy is horizontally or verticallly one direction, so bfs is wasted
        maxVal = 0
        row = 0
        col = [0 for i in xrange(n)]
        
        for i in xrange(m):
            for j in xrange(n):
                # count col
                if i == 0 or grid[i-1][j] == 'W':
                    col[j] = 0
                    for k in xrange(i, m):
                        if grid[k][j] =='E':
                            col[j] += 1
                        if grid[k][j] == 'W':
                            break
    
                # count row
                if j == 0 or grid[i][j-1] == 'W':
                    row = 0
                    for k in xrange(j, n):
                        if grid[i][k] == 'E':
                            row += 1
                        if grid[i][k] == 'W':
                            break
                        
                # print i, j, row, col
                if grid[i][j] == '0' and row+col[j] > maxVal:
                    maxVal = row+col[j]
                    
        return maxVal
                
                
        
                    
                