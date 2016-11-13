# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/build-post-office
@Language: Python
@Datetime: 16-10-19 23:46
'''

import sys
import math

class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        if grid is None or len(grid) == 0:
            return -1
        
        m, n = len(grid), len(grid[0])
        # print m, n
        visited = [[False for i in xrange(n)] for j in xrange(m)]
        houseList = []
        x_list = []
        y_list = []
        i_med = 0.0
        j_med = 0.0
        minD = sys.maxint
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    houseList.append((i, j))
                    x_list.append(i)
                    y_list.append(j)
                    # i_med += i
                    # j_med += j
        if len(houseList) == 0 or len(houseList) == m*n:
            return -1

        # print i_med, j_med, len(houseList)
        # i_med = int(round(i_med/len(houseList)))
        # j_med = int(round(j_med/len(houseList)))
         
        i_med = self.getMedian(x_list)
        j_med = self.getMedian(y_list)
        i_x = [-1, -1, -1, 0, 0, 1, 1, 1] 
        j_y = [-1, 0, 1, -1, 1, -1, 0, 1]
        
        
        minD = sys.maxint

        q = [(i_med, j_med)]
        visited[i_med][j_med] = True
        while len(q) > 0:
            size = len(q)
            for circle in xrange(size):
                i, j = q.pop(0)
                if grid[i][j] == 0:
                    minD = min(minD, self.calculateD(houseList, i, j))

                for node in xrange(8):
                    next_x = i+i_x[node]
                    next_y = j+j_y[node]
                    if self.isEmpty(next_x, next_y, grid) and visited[next_x][next_y] == False:
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y))

            if minD != sys.maxint:
                return minD 
                       
        return -1

    def getMedian(self, array):
        array = sorted(array)

        if len(array)%2 == 0:
            return (array[len(array)/2] + array[len(array)/2-1])/2
        else:
            return array[len(array)/2]


    def isEmpty(self, x, y, grid):
        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) \
            and grid[x][y] == 0:
            return True
        else:
            return False

    def calculateD(self, houseList, i, j):
        d = 0
        for h_x, h_y in houseList:
            d += abs(h_x-i) + abs(h_y-j)

        return d