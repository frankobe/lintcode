# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/palindrome-partitioning
@Language: Python
@Datetime: 15-09-07 22:40
'''

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def isPartition(self, s):
        l = len(s)
        mid = l/2
        
        for i in xrange(mid):
            if s[i] != s[-i-1]:
                return False
        
        return True
        
    def partitionHelper(self, stack, index, result, s):
        n = len(s)
        if index == n:
            result.append(list(stack))
            return
        
        for i in xrange(index, n):
            if self.isPartition(s[index: i+1]):
                stack.append(s[index:i+1])
                self.partitionHelper(stack, i+1, result, s)
                stack.pop()
            
    def partition(self, s):
        # write your code here
        if s is None:
            return None
        
        result = []
        stack = []
        index = 0
        self.partitionHelper(stack, index, result, s)
        
        return result