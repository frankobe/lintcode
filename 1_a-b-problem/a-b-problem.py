# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/a-b-problem
@Language: Python
@Datetime: 16-11-02 19:21
'''

class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        
        MAX_BIT = 2**32
        MAX_BIT_COMPLIMENT = -2**32
        
        while b != 0:
            if b == MAX_BIT:
                return a ^ MAX_BIT_COMPLIMENT
            # XOR = addition without carry
            _a = a^b
            # AND = carry bit
            _b = (a & b) << 1
            a = _a
            b = _b
            
        return a
            