# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/word-ladder-ii
@Language: Python
@Datetime: 15-09-10 00:37
'''

from string import ascii_lowercase
from collections import defaultdict
class Solution:

    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        dict.add(end)
        level = {start}
        size = len(start)
        parents = defaultdict(set)
        while level and end not in parents:
            next_level = defaultdict(set)
            for node in level:
                for char in ascii_lowercase:
                    for i in range(size):
                        n = node[:i]+char+node[i+1:]
                        if n in dict and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res

            
        
                            
                                
        
                        
                        
