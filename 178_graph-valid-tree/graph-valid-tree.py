# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/graph-valid-tree
@Language: Python
@Datetime: 16-04-14 03:40
'''

class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        
        parentDict = {}
        for i in xrange(n):
            parentDict[i] = i
        
        def find(x):
            if parentDict[x] != x:
                parentDict[x] = find(parentDict[x])
                return parentDict[x]
            else:
                return x
                
        def union(x, y):
            px = find(x)
            py = find(y)
            
            if px != py:
                parentDict[px] = py
                
        for e in edges:
            p1 = find(e[0])
            p2 = find(e[1])
            
            if p1 == p2:
                return False
            else:
                union(e[0], e[1])
        
        return len(edges) == n-1
                
        
        