# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/combination-sum
@Language: Python
@Datetime: 15-09-12 23:47
'''

class Solution:
    def findNext(self, tmpList, index, candidates, target, result):
        if index > len(candidates):
            return
    
        if target == 0:
            result.append(list(tmpList))
            return
        
        for i in xrange(index, len(candidates)):
            if target >= candidates[i]:
                tmpList.append(candidates[i])
                self.findNext(tmpList, i, candidates, target - candidates[i] , result)
                tmpList.pop()
            else:
                return
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = sorted(candidates)
        result = []
        self.findNext([], 0, candidates, target, result)
        return result