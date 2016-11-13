# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/search-a-2d-matrix-ii
@Language: Python
@Datetime: 15-06-26 18:20
'''

class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        occurrence = 0
        
        if len(matrix) == 0 or len(matrix[0]) == 0 or target is None:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        
        while x < m and y >= 0:
            if matrix[x][y] == target:
                occurrence += 1
                y -= 1
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
                
                
        return occurrence
        
