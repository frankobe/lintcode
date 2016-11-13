# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/kth-largest-in-n-arrays
@Language: Python
@Datetime: 16-09-29 18:36
'''

from heapq import *

class Solution:
    # @param {int[][]} arrays a list of array
    # @param {int} k an integer
    # @return {int} an integer, K-th largest element in N arrays
    def KthInArrays(self, arrays, k):
        # Write your code here
        heap = []
        for a in arrays:
            for n in a:
                heap.append(-n)
               
        heapify(heap)
        num = None   
        for i in xrange(k):
            num = heappop(heap)
            
        return -num
                