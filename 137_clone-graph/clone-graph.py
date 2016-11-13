# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/clone-graph
@Language: Python
@Datetime: 15-09-06 02:09
'''

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return None
        # clone node
        nodes = []
        nodes.append(node)
        nodeMap = {}
        nodeMap[node] = UndirectedGraphNode(node.label)
        
        start = 0
        while start < len(nodes):
            head = nodes[start]
            start = start + 1
            for i in xrange(len(head.neighbors)):
                neighbor = head.neighbors[i]
                if neighbor not in nodeMap:
                    nodeMap[neighbor] = UndirectedGraphNode(neighbor.label)
                    nodes.append(neighbor)
                    
        # clone neighor
        for i in xrange(len(nodes)):
            head = nodes[i]
            neighborList = head.neighbors
            for j in xrange(len(neighborList)):
                nodeMap[head].neighbors.append(nodeMap[neighborList[j]])
                
        return nodeMap[node]
        
         
                   
        
            
        