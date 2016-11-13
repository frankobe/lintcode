# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/minimum-window-substring
@Language: Python
@Datetime: 16-05-04 06:30
'''

class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        
        target_d = {}
        for i in target:
            if i in target_d:
                target_d[i] += 1
            else:
                target_d[i] = 1
        d = {}
        n = len(source)
        j = 0
        left, right = 0, n+1
        for i in xrange(n):
            while j < n and not self.compare(target_d, d): 
                if source[j] in target:
                    if source[j] in d:
                        d[source[j]] += 1
                    else:
                        d[source[j]] = 1
                        
                j += 1
                
            
            if self.compare(target_d, d) and right - left > j - i:
                left, right = i, j
                
            if source[i] in d:
                d[source[i]] -= 1
                if d[source[i]] == 0:
                    del d[source[i]]
                   
        return "" if right == n+1 else source[left:right]
        
    def compare(self, target, di):
        for k, v in target.iteritems():
            if k in di:
                if v > di[k]:
                    return False
            else:
                return False
                
        return True
                