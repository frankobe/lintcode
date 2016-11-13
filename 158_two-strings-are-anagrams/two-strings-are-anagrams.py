# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/two-strings-are-anagrams
@Language: Python
@Datetime: 16-02-28 02:00
'''

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        if s is None and t is None:
            return True
        
        if len(s) == 0 and len(t) == 0:
            return True
        
        if s is None or len(s) == 0 or t is None or len(t) == 0:
            return False
        
        if len(s) != len(t):
            return False
            
        table = [0]*256
        for i in xrange(len(s)):
            index = ord(s[i])
            table[index] = table[index] + 1
        
        for i in xrange(len(t)):
            index = ord(t[i])
            table[index] = table[index] - 1
            if table[index] < 0:
                return False
                
        return True