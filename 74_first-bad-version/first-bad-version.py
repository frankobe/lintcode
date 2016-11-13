# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/first-bad-version
@Language: Python
@Datetime: 15-06-26 18:37
'''

#class VersionControl:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use VersionControl.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        if n < 1:
            return -1
        
        start, end = 1, n 
        
        while start + 1 < end:
            mid = (start + end) / 2
            
            if VersionControl.isBadVersion(mid):
                end = mid
            
            else:
                start = mid
                
        
        if VersionControl.isBadVersion(start):
            return start
        
        elif VersionControl.isBadVersion(end):
            return end
            
        else:
            return -1