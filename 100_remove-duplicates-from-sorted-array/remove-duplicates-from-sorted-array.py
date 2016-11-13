# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-sorted-array
@Language: Python
@Datetime: 16-02-28 10:15
'''

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 0
        
        h, t = 0, 1
        while t < len(A):
            if A[h] == A[t]:
                t += 1
            else:
                A[h+1] = A[t]
                h += 1
                t += 1
                
        return h + 1
        