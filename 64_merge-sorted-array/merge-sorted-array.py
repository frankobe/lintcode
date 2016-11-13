# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/merge-sorted-array
@Language: Python
@Datetime: 15-06-28 01:21
'''

class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        index ,i, j = n + m -1, m - 1, n - 1
        
        while i >=0 and j >= 0:
            if A[i] >= B[j]:
                A[index] = A[i]
                index -= 1
                i -= 1
            else:
                A[index] = B[j]
                index -= 1
                j -= 1
            
        while j >= 0:
            A[index] = B[j]
            index -= 1
            j -= 1
        