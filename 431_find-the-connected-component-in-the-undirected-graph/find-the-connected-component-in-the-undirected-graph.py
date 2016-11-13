# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/find-the-connected-component-in-the-undirected-graph
@Language: Python
@Datetime: 16-02-22 03:19
'''

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        # Write your code here
        dictionary = {}
        for node in nodes:
            if node not in dictionary:
               self.dfs(node, node, dictionary)
                    
        result = {}
        for k, v in dictionary.iteritems():
            if v in result:
                result[v].append(k.label)
            else:
                result[v] = [k.label]
        
        return [sorted(x) for x in result.values()]
        
    def dfs(self, parent, node, dictionary):
        if node not in dictionary:
            dictionary[node] = parent
            
        for neighbor in node.neighbors:
            if neighbor not in dictionary:
                self.dfs(parent, neighbor, dictionary)
                
            
        
            
                    
            