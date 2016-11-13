# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/topological-sorting
@Language: Python
@Datetime: 15-09-06 18:49
'''

# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def dfs(self, degreeMap, tmpNode, result):
        result.append(tmpNode)
        degreeMap[tmpNode] = degreeMap[tmpNode] - 1 #avoid duplication 
        for tmpNeighbor in tmpNode.neighbors:
            degreeMap[tmpNeighbor] = degreeMap[tmpNeighbor] - 1
            if degreeMap[tmpNeighbor] == 0:
                self.dfs(degreeMap, tmpNeighbor, result)

    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        # write your code here
        
        if graph is None:
            return None
            
        result = []
        degreeMap = {}
        
        for tmpNode in graph:
            if tmpNode not in degreeMap:
                degreeMap[tmpNode] = 0
            for tmpNeighbor in tmpNode.neighbors:
                if tmpNeighbor in degreeMap:
                    degreeMap[tmpNeighbor] = degreeMap[tmpNeighbor] + 1
                else:
                    degreeMap[tmpNeighbor] = 1
                    
        #DFS
        for tmpNode in graph:
            if degreeMap[tmpNode] == 0:
                self.dfs(degreeMap, tmpNode, result)
                
        return result
                
        #BFS
        queue = [] 
        for tmpNode in graph:
            if degreeMap[tmpNode] == 0:
                result.append(tmpNode)
                queue.append(tmpNode)
       
        while len(queue) != 0:
            tmpNode = queue.pop(0)
            for tmpNeighbor in tmpNode.neighbors:
                degreeMap[tmpNeighbor] = degreeMap[tmpNeighbor] - 1
                if degreeMap[tmpNeighbor] == 0:
                    queue.append(tmpNeighbor)
                    result.append(tmpNeighbor)
          
        return result
        
            
        