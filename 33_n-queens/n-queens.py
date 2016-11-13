# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/n-queens
@Language: Python
@Datetime: 15-09-07 21:07
'''

class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    
    def drawChessBoard(self, config):
        n = len(config)
        chessboard = [""]*n
        for i in xrange(n):
            for j in xrange(n):
                if j == config[i]:
                    chessboard[i] += "Q"
                else:
                    chessboard[i] += "."
                    
        return chessboard
        
    def isValid(self, stack, col):
        if len(stack)==0:
            return True
            
        upLeftToBottomRight = len(stack) - col
        upRightToBottomLeft = len(stack) + col
        
        for i in xrange(len(stack)):
            if upLeftToBottomRight == i-stack[i] or upRightToBottomLeft == i + stack[i]:
                return False
        return True
        
    def search(self, stack, n, result):
        if len(stack) == n:
            result.append(self.drawChessBoard(stack))
            return 
            
        for col in xrange(n):
            if col not in stack and self.isValid(stack, col):
                stack.append(col)
                self.search(stack, n, result)
                stack.pop()
    
    def solveNQueens(self, n):
        # write your code here
        if n <= 0:
            return None
        result = []
        self.search([],n,result)
        return result
            
        

