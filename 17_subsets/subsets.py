# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/subsets
@Language: Python
@Datetime: 15-09-07 18:58
'''

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    # def subsetsHelper(self, result, subset, S, index):
        
    #     result.append(list(subset))
        
    #     for i in range(index, len(S)):
    #         subset.append(S[i])
    #         self.subsetsHelper(result, subset, S, i+1)
    #         subset.pop()
        
    # def subsets(self, S):
    #     # write your code here
            
    #     S.sort()       
    #     result = [];
    #     self.subsetsHelper(result, [], S, 0)
    #     return result
    
    def subsets(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, subSet, res):
        res.append(list(subSet)) 
        for i in xrange(index, len(nums)):
            subSet.append(nums[i])
            self.dfs(nums, i+1, subSet, res)
            subSet.pop()
