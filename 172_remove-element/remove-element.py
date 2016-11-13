# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/remove-element
@Language: Python
@Datetime: 16-02-28 10:08
'''

class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        
        if A is None or len(A) == 0 or elem is None:
            return 0
        
        head, tail = 0, len(A) - 1
        while head <= tail:
            if A[head] == elem:
                A[head] = A[tail]
                tail -= 1
            else:
                head +=1
        
        return tail+1