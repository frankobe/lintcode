# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/trapping-rain-water
@Language: Python
@Datetime: 16-04-18 20:29
'''

class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        if heights is None:
            return 0
            
        l,r = 0, len(heights)-1
        if r == -1:
            return 0
            
        count = 0
        hl, hr = heights[l], heights[r]
    
        while l < r:
            if hl < hr:
                if heights[l+1] > hl:
                    hl = heights[l+1]
                else:
                    count += hl - heights[l+1]
                l +=1
            else:
                if heights[r-1] > hr:
                    hr = heights[r-1]
                else:
                    count += hr - heights[r-1]
            
                r -= 1
        
        return count