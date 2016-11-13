# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/triangle-count
@Language: Python
@Datetime: 16-09-29 21:24
'''

class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        # write your code here
        if S is None or len(S) < 3:
            return 0
            
        S.sort()
        # count = 0
        
        # for i in xrange(0, len(S)-2):
        #     p1 = i + 1
        #     p2 = i + 2
        #     while p1 < len(S)-1:
        #         while p2 < len(S) and S[i] + S[p1] > S[p2]:
        #             p2 += 1

        #         count += p2 - p1 -1
        #         p1 += 1
        # return count
        left = 0
        right = len(S) - 1
        ans = 0
        for i in xrange(2, len(S)):
            left = 0
            right = i - 1;
            while(left < right):
                if(S[left] + S[right] > S[i]):
                    ans = ans + (right - left)
                    right -=1
                else:
                    left +=1
                
            
        return ans;