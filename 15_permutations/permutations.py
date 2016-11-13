# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/permutations
@Language: Python
@Datetime: 15-09-07 18:45
'''

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    
    def permuteHelper(self, nums, result, tmpList):
        if len(tmpList) == len(nums):
            result.append(list(tmpList))
            return
        
        for num in nums:
            if num not in tmpList:
                tmpList.append(num)
                self.permuteHelper(nums, result, tmpList)
                tmpList.pop() 
            
    def permute(self, nums):
        # write your code here
        if nums is None:
            return []
        n = len(nums)
        stack = [-1]
        permutations = []
        while len(stack):
            last = stack.pop()
            next = -1
            for i in xrange(last+1, n):
                if i not in stack:
                    next = i
                    break

            if next == -1:
                continue

            stack.append(next)
            for i in xrange(n):
                if i not in stack:
                    stack.append(i)

            permutation = []
            for i in xrange(n):
                permutation.append(nums[stack[i]])
            
            # print stack
            # print permutation
            permutations.append(list(permutation))
            
        return permutations
    

            