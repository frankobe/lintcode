# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/largest-rectangle-in-histogram
@Language: Python
@Datetime: 15-09-14 16:03
'''

class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        
        #solution 1
        # n = len(height)
        # maxV = 0
        # for i in xrange(n):
        #     if i+1 < n and height[i+1] >= height[i]:
        #         continue
        #     minH = height[i]
        #     for j in xrange(i, -1, -1):
        #         minH = min(minH, height[j])
        #         maxV = max(maxV, minH*(i-j+1))
        
        # return maxV
        
        stack = []
        newHeight = list(height)
        newHeight.append(0)
        n = len(newHeight)
        maxRect = 0
        i = 0
        
        while i < n:
            if len(stack) == 0 or newHeight[stack[-1]] <= newHeight[i]:
                stack.append(i)
                i += 1
            else:
                topIndex = stack.pop()
                if len(stack) == 0:
                    maxRect = max(maxRect, newHeight[topIndex]*i)
                else:
                    maxRect = max(maxRect, newHeight[topIndex]*(i-stack[-1]-1))
                
        return maxRect
        
        
        
        
