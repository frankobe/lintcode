# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/number-of-islands-ii
@Language: Python
@Datetime: 16-03-28 00:56
'''

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def __init__(self):
        self.f = {}
        
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Point[]} operators an array of point
    # @return {int[]} an integer array
    def numIslands2(self, n, m, operators):
        # Write your code here
        if n < 0 or m < 0:
            return []
            
        for i in xrange(n*m):
                self.f[i] = -1
                
        result = []
        d = [[-1,0],[0,-1], [1,0], [0,1]]
        area = 0
        
        def index(p):
            return p.x * m + p.y
            
        def check(p):
            return p.x >= 0 and p.x < n and p.y >= 0 and p.y < m
            
        for o in operators:
            if check(o):
                if self.f[index(o)] == -1:
                    area += 1
                    self.f[index(o)] = index(o)
                    
                for i in xrange(4):
                    nextP = Point(o.x+d[i][0], o.y+d[i][1])
                    if check(nextP):
                        if self.merge(index(nextP), index(o)):
                            area -= 1
                
            result.append(area)
                
        return result
                        
    
    # Union set
    def find(self, x):
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
        
    def merge(self, x, y):
        if self.f[x] == -1 or self.f[y] == -1:
            return False
        
        x = self.find(x)
        y = self.find(y)
        
        if x != y:
            self.f[x] = y
            return True
        else:
            return False
    
    # def countNum(self, x):
        