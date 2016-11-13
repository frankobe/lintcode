# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/surrounded-regions
@Language: Python
@Datetime: 16-03-28 04:42
'''

class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing 
    def surroundedRegions(self, board):
        # Write your code here
        n = len(board)
        if n == 0:
            return
        
        m = len(board[0])
        d = [(-1,0), (0,-1), (1,0), (0,1)]
        q = []
        
        def check(x,y):
            return x >= 0 and y >= 0 and x < n and y < m and board[x][y] == 'O'
            
        def fill(x, y):
            if x < 0 or x > n-1 or y < 0 or y > m-1 or board[x][y] != 'O':
                return
            q.append((x,y))
            board[x][y] = 'V'
        
        def dfs(x, y):
            if not check(x, y):
                return 
            
            board[x][y] = 'V';
            for i in xrange(4):
                nextX = x + d[i][0]
                nextY = y + d[i][1]
                dfs(nextX, nextY)
            
        # dfs 
        # for i in xrange(n):
        #     for j in xrange(m):
        #         if i == 0 or j == 0 or i == n-1 or j == m -1:
        #             dfs(i, j)
        
        # bfs 
        for i in xrange(n):
            for j in xrange(m):
                if i == 0 or j == 0 or i == n-1 or j == m-1:
                    fill(i, j)
        while q:
            node = q.pop(0)
            fill(node[0]-1, node[1])
            fill(node[0]+1, node[1])
            fill(node[0], node[1]-1)
            fill(node[0], node[1]+1)
                
        for i in xrange(n):
            for j in xrange(m):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                    
        
                    
                    
                
        
        