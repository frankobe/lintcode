# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/kth-largest-element
@Language: Python
@Datetime: 16-04-04 05:19
'''

import heapq

class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if A is None or len(A) < k:
            return 0
            
        heapq.heapify(A)
        t = None
        for i in xrange(len(A) - k+1):
            t = heapq.heappop(A)
        
        return t