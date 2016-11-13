# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/find-the-weak-connected-component-in-the-directed-graph
@Language: Python
@Datetime: 16-03-28 01:06
'''

# Definition for a directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class DirectedGraph:
    def __init__(self, nodes):
        self.father = {}
        for node in nodes:
            self.father[node] = node
            
    def find(self, x):
        # parent = self.father[x]
        # tmpQ = set()
        # while parent != self.father[parent]:
        #     tmpQ.add(parent)
        #     parent = self.father[parent]
            
        # for node in tmpQ:
        #     self.father[node] = parent
        
        # return parent
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.father[fx] = fy
        
class Solution:
    # @param {DirectedGraphNode[]} nodes a array of directed graph node
    # @return {int[][]} a connected set of a directed graph
    def connectedSet2(self, nodes):
        # Write your code here
        dg = DirectedGraph(nodes)

        for node in nodes:
            for n in node.neighbors:
                dg.union(node, n)

        return self.helper(dg)
                
    def helper(self, dg):
        neighDict = {}
        for l in dg.father:
            fa = dg.find(l)
            if fa in neighDict:
                neighDict[fa].append(l.label)
            else:
                neighDict[fa] = [l.label]

        for v in neighDict.values():
            v.sort()

        return neighDict.values()