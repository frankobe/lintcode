# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters
@Language: Python
@Datetime: 16-05-03 18:00
'''

class Solution:
    # @param s : A string
    # @return : An integer
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if s is None or len(s) == 0 or k == 0:
            return 0
        n = len(s)            
        l = {}
        maxLen = 0
        j = 0
        for i in xrange(n):
            while j < n and len(l) <= k:
                if s[j] in l or \
                    s[j] not in l and len(l) < k:
                    l[s[j]] = j
                    j += 1
                else:
                    break
                    
            maxLen = max(maxLen, j-i)
            if j == n:
                break
            
            if s[i] in l and i >= l[s[i]]:
                del l[s[i]]
                
        return maxLen