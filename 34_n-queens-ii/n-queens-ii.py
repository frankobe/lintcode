# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/n-queens-ii
@Language: Python
@Datetime: 15-09-07 22:17
'''

class Solution:
    """
    Calculate the total number of distinct N-Queen solutions.
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    sum  = 0
    def isValid(self, col, stack):
        n = len(stack)
        sub  = n - col
        sumCol = n + col
        
        for i in xrange(n):
            if i + stack[i] == sumCol or i - stack[i] == sub:
                return False
        return True
    
    def search(self, n, stack):
        if len(stack) == n:
            self.sum += 1
            return 
        
        for col in xrange(n):
            if col not in stack and self.isValid(col, stack):
                stack.append(col)
                self.search(n, stack)
                stack.pop()
        
    def totalNQueens(self, n):
        # write your code here
        if n <= 0:
            return None

        self.search(n, [])
        return self.sum

