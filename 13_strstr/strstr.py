# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/strstr
@Language: Python
@Datetime: 16-02-28 03:23
'''

class Solution:
    def strStr(self, source, target):
        # write your code here
        
        if target is None or source is None:
            return -1
            
        if len(target) == 0:
            return 0
            
        for i in xrange(len(source) - len(target)+1):
            for j in xrange(len(target)):
                if source[i+j] != target[j]:
                    break;
                    
            if j == len(target) - 1 and source[i+j] == target[j]:
                return i
                
        return -1
        
        
