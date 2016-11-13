# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/min-stack
@Language: Python
@Datetime: 15-09-13 04:53
'''

class MinStack(object):

    minValue = None
    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.minVal = []
        
    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if len(self.minVal) == 0 or number <= self.minVal[-1]:
            self.minVal.append(number)
        
    def pop(self):
        # pop and return the top item in stack
        if self.minVal[-1] == self.stack[-1]:
            self.minVal.pop()
        return self.stack.pop()
    
    def min(self):
        # return the minimum number in stack
        return self.minVal[-1]