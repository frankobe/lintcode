# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/container-with-most-water
@Language: Python
@Datetime: 16-05-01 01:55
'''

class Solution:
    # @param heights: a list of integers
    # @return: an integer
    def maxArea(self, heights):
        # write your code here
        maxArea = 0
        left, right = 0, len(heights)-1
        while left < right:
            minEdge = min(heights[left], heights[right])
            area = (right-left)*minEdge
            maxArea = max(maxArea, area)
            if minEdge == heights[left]:
                next_left = left+1
                while next_left < right and heights[next_left] <= heights[left]:
                    next_left += 1
                left = next_left 
            else:
                next_right = right-1
                while next_right > left and heights[next_right] <= heights[right]:
                    next_right -= 1
                right = next_right
        return maxArea