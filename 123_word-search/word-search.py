# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/word-search
@Language: Python
@Datetime: 16-04-14 21:23
'''

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        # write your code here
        if word is None or len(word) == 0:
            return True
            
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return False
            
        m, n = len(board), len(board[0])
        
        visited = [[False for i in xrange(n)] for j in xrange(m)]
            
        for i in xrange(m):
            for j in xrange(n):
               if self.dfs(i, j, board, word, visited):
                   return True
                
        return False
        
        
    def dfs(self, i, j, board, word, visited):
        if len(word) == 0:
            return True
        
        if self.check(i, j, board, visited):    
            if word[0] == board[i][j]:
                visited[i][j] = True
                mx = [-1, 0, 0, 1]
                my = [0, -1, 1, 0]
                if self.dfs(i + mx[0], j + my[0], board, word[1:], visited) or \
                   self.dfs(i + mx[1], j + my[1], board, word[1:], visited) or \
                   self.dfs(i + mx[2], j + my[2], board, word[1:], visited) or \
                   self.dfs(i + mx[3], j + my[3], board, word[1:], visited):
                    return True
                else:
                    visited[i][j] = False
        return False
        
    def check(self, i, j, board, visited):
        m, n = len(board), len(board[0])
        if i >=0 and i < m and j >= 0 and j < n:
            return not visited[i][j]
        else:
            return False