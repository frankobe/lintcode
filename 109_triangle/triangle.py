# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/triangle
@Language: Python
@Datetime: 15-07-27 06:18
'''

class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    
    def dfs(self, x, y, minSum, triangle):
        if x >= len(triangle):
            return 0
        
        if minSum[x][y] is None:
            minSum[x][y] = min(self.dfs(x+1,y, minSum, triangle), self.dfs(x+1,y + 1, minSum, triangle)) + triangle[x][y]
            
        return minSum[x][y]
            
    
    def minimumTotal(self, triangle):
        # write your code here
        if triangle is None or len(triangle) == 0:
            return 0
        n = len(triangle)
        
        minSum = [[None for i in range(n)] for j in range(n)]
        return self.dfs(0,0,minSum,triangle)
        
        
    