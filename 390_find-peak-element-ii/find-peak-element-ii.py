# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/find-peak-element-ii
@Language: Python
@Datetime: 16-10-08 00:47
'''

class Solution:
    #@param A: An list of list integer 
    #@return: The index of position is a list of integer, for example [2,2]
    def findPeakII(self, A):
        # write your code here
        if A is None or len(A) == 0 or len(A) < 3 \
            or A[0] is None or len(A[0]) == 0 or len(A[0]) < 3:
            return None

        return self.helper(0, len(A), 0, len(A[0]), A)
                
    def helper(self, m_start, m_end, n_start, n_end, A):
        if m_end - m_start < 2 or n_end - n_start < 2:
            return None
        
        mid_m, mid_n = (m_start+m_end)/2, (n_start+n_end)/2
        i, j = self.findPeak(mid_m, mid_n, A)
        if self.isPeak(i, j, A):
            return [i,j]
        elif i == mid_m:
            if j < mid_n:
                if A[i][j] > A[i-1][j]:
                    return self.helper(mid_m, m_end, n_start, mid_n, A)
                else:
                    return self.helper(m_start, mid_m, n_start, mid_n, A)
            else:
                if A[i][j] > A[i-1][j]:
                    return self.helper(mid_m, m_end, mid_n, n_end, A)
                else:
                    return self.helper(m_start, mid_m, mid_n, n_end, A)
        else:
            if i < mid_m:
                if A[i][j] > A[i][j-1]:
                    return self.helper(m_start, mid_m, mid_n, n_end, A)
                else:
                    return self.helper(m_start, mid_m, n_start, mid_n, A)
            else:
                if A[i][j] > A[i][j-1]:
                    return self.helper(mid_m, m_end, mid_n, n_end, A)
                else:
                    return self.helper(mid_m, m_end, n_start, mid_n, A)

    def findPeak(self, m, n, A):
        # find the index of max val in m-th col and n-th row
        maxVal = 0
        x, y = None, None
        for i in xrange(len(A)):
            if A[i][n] > maxVal:
                maxVal = A[i][n]
                x, y = i,n
                
        for j in xrange(len(A[0])):
            if A[m][j] > maxVal:
                maxVal = A[m][j]
                x, y = m , j
        
        return x, y
    
    def isPeak(self, i, j, A):
        if i > 0 and i < len(A)-1 and j > 0 and j < len(A[0])-1:
            if A[i][j] > A[i+1][j] and A[i][j] > A[i-1][j] and A[i][j] > A[i][j+1] and A[i][j] > A[i][j-1]:
                return True
        return False