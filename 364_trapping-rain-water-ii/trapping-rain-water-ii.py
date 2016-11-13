# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/trapping-rain-water-ii
@Language: Python
@Datetime: 16-04-19 07:12
'''

import heapq

class Solution:
    # @param heights: a matrix of integers
    # @return: an integer
    def trapRainWater(self, heights):
        # write your code here
        if heights is None:
            return 0
            
        m, n = len(heights), len(heights[0])
        if m < 3 or n < 3:
            return 0
        
        visited = [[False for i in xrange(n)] for j in xrange(m)]
            
        h = []
        for i in xrange(n):
            heapq.heappush(h, (heights[0][i], 0, i))
            heapq.heappush(h, (heights[m-1][i], m-1, i))
            
            visited[0][i] = True
            visited[m-1][i] = True
            
        for i in xrange(1, m-1):
            heapq.heappush(h, (heights[i][0], i, 0))
            heapq.heappush(h, (heights[i][n-1], i, n-1))
            
            visited[i][0] = True
            visited[i][n-1] = True
        
        # print h
        
        result = 0
        direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        while len(h) > 0:
            height, dx, dy = heapq.heappop(h)
            # print height, dx, dy
            for k in xrange(4):
                nx = dx + direction[k][0]
                ny = dy + direction[k][1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                    continue
                    
                heapq.heappush(h, (max(height, heights[nx][ny]), nx, ny))
                visited[nx][ny] = True
                result += max(0, height - heights[nx][ny])
                
        return result