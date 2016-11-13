# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/subarray-sum-ii
@Language: Python
@Datetime: 16-10-12 19:31
'''

import math
import bisect
class Solution:
    # @param {int[]} A an integer array
    # @param {int} start an integer
    # @param {int} end an integer
    # @return {int} the number of possible answer
    def subarraySumII(self, A, start, end):
        # Write your code here
        if A is None or len(A) == 0:
            return 0
        
        l = len(A)
        
        res = 0
        f = [0]*(l+1)
        for i in xrange(1, l+1):
            f[i] = f[i-1] + A[i-1]

# hand code version
        # for i in xrange(l):
        #     lo, hi = i+1, l
        #     # find left bound
        #     while lo < hi:
        #         # print lo, hi
        #         mid = (lo+hi)/2
        #         if f[mid] - f[i] < start:
        #             lo = mid+1
        #         else:
        #             hi = mid

        #     if f[lo] - f[i] >= start and f[lo] - f[i] <= end:
        #         left = lo
        #     elif f[hi] - f[i] >= start and f[hi] - f[i] <= end:
        #         left = hi
        #     else:
        #         break

        #     lo, hi = i+1, l
        #     while lo < hi:
        #         # print lo, hi
        #         mid = int(math.ceil((lo+hi)/2.0))
        #         if f[mid] - f[i] > end:
        #             hi = mid-1
        #         else:
        #             lo = mid

        #     if f[hi] - f[i] >= start and f[hi] - f[i] <= end:
        #         right = hi
        #     elif f[lo] - f[i] >= start and f[lo] - f[i] <= end:
        #         right = lo
        #     else:
        #         break
            
        #     res = res + right -left+1
        
        for i in xrange(l):
            left = bisect.bisect_left(f, start+f[i], i+1)
            right = bisect.bisect_right(f, end+f[i], i+1)
            res = res + right - left
        return res