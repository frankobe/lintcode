# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array-ii
@Language: Python
@Datetime: 16-02-04 19:23
'''

class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if num is None or len(num) == 0:
            return None
        
        return self.iterator(num, 0, len(num)-1)
    
    def iterator(self, num, start, end):
        if start + 1 >= end:
            return min(num[start], num[end])
        
        mid = (start+end)/2
        
        if num[start] > num[mid]:
            return self.iterator(num,start,mid)
        elif num[end] < num[mid]:
            return self.iterator(num,mid,end)
        elif num[start] < num[mid] and num[mid] < num[end]:
            return num[start]
        else:
            return min(self.iterator(num, start, mid), self.iterator(num, mid, end))