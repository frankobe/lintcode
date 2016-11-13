# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/word-break
@Language: Python
@Datetime: 16-02-23 07:47
'''

class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    
    # return the max word len in dict

    # def wordBreak(self, s, dict):
    #     # write your code here
    #     if s is None or len(s) == 0:
    #         return True
    #     if dict is None or len(dict) == 0:
    #         return False
        
    #     max_word_len = max([len(w) for w in dict])
    #     can_break = [True]
    #     for i in xrange(len(s)):
    #         can_break.append(False)
    #         for j in xrange(i, -1, -1):
    #             # optimize for too long interval
    #             if i - j + 1 > max_word_len:
    #                 break
    #             if can_break[j] and s[j:i + 1] in dict:
    #                 can_break[i + 1] = True
    #                 break
    #     return can_break[-1]
    
    def wordBreak(self, s, dict):
        # write your code here
        if s is None or len(s) == 0:
            return True
        
        if dict is None or len(dict) == 0:
            return False
            
        max_word_len = max([len(w) for w in dict])
        can_break = [True]
        for i in xrange(len(s)):
            can_break.append(False)
            for j in xrange(i, -1, -1):
                if i - j + 1 > max_word_len:
                    break
                if can_break[j] and s[j:i+1] in dict:
                    can_break[i+1] = True
                    break
        return can_break[-1]
            
