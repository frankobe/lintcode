# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/longest-palindromic-substring
@Language: Python
@Datetime: 16-07-05 16:01
'''

class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        # Write your code her
        
        if s is None or len(s) == 0:
            return None
            
        new_str = '#'
        ans = ''
        for c in s:
            new_str += c
            new_str += '#'
            
        maxl = 0 
        for i in xrange(len(new_str)):
            start = i
            end = i
            while start-1 >=0 and end+1 < len(new_str):
                if new_str[start-1] == new_str[end+1]:
                    start -= 1
                    end += 1
                else:
                    break
            currentl = end/2 - start/2
            if currentl > maxl:
                maxl = currentl
                ans = s[start/2:end/2]
                
        return ans