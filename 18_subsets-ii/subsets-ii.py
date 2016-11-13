# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/subsets-ii
@Language: Python
@Datetime: 15-06-22 21:39
'''

class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        S.sort()
        result = []
        self.subsetsHelper(S, result, [], 0)
        
        return result
        
    def subsetsHelper(self, S, result, tmpList, index):
        result.append(list(tmpList))
        
        for i in range(index, len(S)):
            
            if i != index and S[i] == S[i-1]:
                continue
            
            tmpList.append(S[i])
            self.subsetsHelper(S, result, tmpList, i+1)
            tmpList.pop()
            
                