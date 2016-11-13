# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/house-robber
@Language: Python
@Datetime: 16-10-03 18:30
'''

class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 0
        
        dp = [A[0], None]
        for i in xrange(1, len(A)):
            if i - 2 >= 0:
                dp[i%2] = max(dp[(i-1)%2], dp[(i-2)%2]+A[i])
            else:
                dp[i%2] = A[i%2]
        
        if len(A) > 2:
            return max(dp[0], dp[1])
        else:
            return dp[0]