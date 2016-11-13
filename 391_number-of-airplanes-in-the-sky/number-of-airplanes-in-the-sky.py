# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/number-of-airplanes-in-the-sky
@Language: Python
@Datetime: 16-04-14 04:21
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # write your code here
        if airplanes is None or len(airplanes) == 0:
            return 0
            
        data = []
        for a in airplanes:
            data.append((a.start, 1))
            data.append((a.end, -1))
            
        heapq.heapify(data)
        
        count = 0
        maxcount = 0
        
        while len(data) > 0:
            a = heapq.heappop(data)
            count += a[1]
            if count > maxcount:
                maxcount = count
        
        return maxcount