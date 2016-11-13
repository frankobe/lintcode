# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/sliding-window-maximum
@Language: Python
@Datetime: 16-04-22 19:22
'''

from collections import deque
class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        q = deque()
        result = []
        for i in xrange(len(nums)):
            while len(q) and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

            if i < k-1:
                continue

            while len(q) and q[0] <= i - k:
                q.popleft()
            
            result.append(nums[q[0]])
            
        return result