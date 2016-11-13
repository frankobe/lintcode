# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/sort-integers-ii
@Language: Python
@Datetime: 16-10-25 00:05
'''

class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        
        if A is None or len(A) == 0:
            return A
            
        # self.mergesort(A, 0, len(A))
        self.quicksort(A, 0, len(A)-1)
        
    def quicksort(self, A, l, r):
        if l < r:
            p = self.partition(A, l, r)
            self.quicksort(A, l, p)
            self.quicksort(A, p+1, r)
            
    def partition(self, A, l, r):
        p = A[l]
        lo, hi = l, r
        while lo < hi:
            while A[hi] >= p and hi > lo:
                hi -= 1
            
            A[lo], A[hi] = A[hi], A[lo]
            
            while A[lo] <= p and lo < hi:
                lo += 1
                
            A[lo], A[hi] = A[hi], A[lo]
        
        if A[lo] == p:
            return lo
        else:
            return hi
    
    def mergesort(self, A, l, r):
        if l + 1 < r:
            mid = (l+r)/2
            self.mergesort(A, l, mid)
            self.mergesort(A, mid, r)
            self.merge(A, l, mid, r)

    def merge(self, A, start, mid, end):
        left = A[start:mid]
        right = A[mid:end]
        i = start
        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                A[i]=right.pop(0)
            else:
                A[i]=left.pop(0)
                
            i += 1
    
        if len(left) > 0:
            for j in xrange(i, end):
                A[j] = left[j-i]
    
        if len(right) > 0:
            for j in xrange(i, end):
                A[j] = right[j-i]
    