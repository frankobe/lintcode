# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/edit-distance
@Language: Python
@Datetime: 15-08-18 22:46
'''

class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        lWord1, lWord2 = len(word1), len(word2)
        if len(word1) == 0:
            return lWord2
        
        if len(word2) == 0:
            return lWord1
        
        # init
        list = [[0 for i in xrange(lWord2+1)] for j in xrange(lWord1+1)]
        
        for i in xrange(lWord1+1):
            list[i][0] = i
        
        for j in xrange(lWord2+1):
            list[0][j] = j
        
        for i in xrange(1, lWord1+1):
            for j in xrange(1, lWord2+1):
                if word1[i-1] == word2[j-1]:
                    list[i][j] = min(list[i-1][j-1], list[i][j-1]+1, list[i-1][j]+1)
                else:
                    list[i][j] = min(list[i-1][j-1], list[i][j-1], list[i-1][j]) + 1
                    
        return list[lWord1][lWord2]
                
        