# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/longest-substring-without-repeating-characters
@Language: Python
@Datetime: 16-05-02 17:12
'''

class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        # write your code here
        
        if s is None or len(s) == 0:
            return 0
            
        maxLen = 1
        left, right = 0, 1
        appear = {s[0]:0}
        while right < len(s):
            if s[right] in appear:
                left = max(appear[s[right]]+1, left)
            
            maxLen = max(maxLen, right - left + 1)
            appear[s[right]] = right
            right += 1
            # print left, right
        return maxLen
            
                