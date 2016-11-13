# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/median-of-two-sorted-arrays
@Language: Python
@Datetime: 16-04-04 01:45
'''

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        n = len(A) + len(B)
        if n < 1:
            return 0
        
        if n%2 == 1:
            return self.findKthSmallest(A, B, n/2+1)
        else:
            return (self.findKthSmallest(A, B, n/2)+self.findKthSmallest(A, B, n/2+1))/2.0
            
    def findKthSmallest(self, A, B, k):
        # k starting from 1
        m, n = len(A), len(B)
        if m == 0:
            return B[k-1]
        
        if n == 0:
            return A[k-1]
            
        if k == 1:
            return min(A[0], B[0])
        
        # if m < k/2:
        #     return self.findKthSmallest(A, B[k/2:], k - k/2)
        # if n < k/2:
        #     return self.findKthSmallest(A[k/2:], B, k - k/2)
            
        
        # if A[k/2 - 1] > B[k/2 - 1]:
        #     return self.findKthSmallest(A, B[k/2:], k - k/2)
        # else:
        #     return self.findKthSmallest(A[k/2:], B, k - k/2)
        
        m, n= max(A[-1], B[-1]), min(A[0], B[0])
        mid = (m+n)/2
        
        na = self.numberLessThan(A, mid)
        nb = self.numberLessThan(B, mid)
        
        if na + nb < k:
            return self.findKthSmallest(A[na:], B[nb:], k - na -nb)
        elif na + nb > k:
            return self.findKthSmallest(A[:na], B[:nb], k)
        else:
            if na == 0:
                return B[k-1]
            elif nb == 0:
                return A[k-1]
            else:
                return max(A[na-1], B[nb-1])
            
        
    def numberLessThan(self, A, num):
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            if A[0] <= num:
                return 1
            else:
                return 0
                
        if A[n/2] <= num:
            return n/2+1+self.numberLessThan(A[n/2+1:], num)
        else:
            return self.numberLessThan(A[:n/2], num)
        
            
    
            