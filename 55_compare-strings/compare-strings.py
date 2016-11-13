# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/compare-strings
@Language: Python
@Datetime: 16-02-28 02:00
'''

class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        
        if B is None or len(B) == 0:
            return True
        
        if A is None or len(A)==0:
            return False
        
        hit = [0] * 26
        
        for i in xrange(len(A)):
            index = ord(A[i]) - ord('A')
            hit[index] = hit[index] + 1
        
        for i in xrange(len(B)):
            index = ord(B[i]) - ord('A')
            hit[index] = hit[index] - 1
            if hit[index] < 0:
                return False
                
        return True
        