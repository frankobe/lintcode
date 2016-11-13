# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/wood-cut
@Language: Python
@Datetime: 16-02-04 18:52
'''

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if L is None or len(L) is None or sum(L) < k or k <= 0:
            return 0
            
        start, end = 1, sum(L)
        
        while start + 1 < end:
            mid = (start+end)/2
            piecesCount = sum([l / mid for l in L])
            if piecesCount >= k:
                start = mid
            else:
                end = mid
                
        if sum([l/end for l in L]) >= k:
            return end
        else:
            return start
            