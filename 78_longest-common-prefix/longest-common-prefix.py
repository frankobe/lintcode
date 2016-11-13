# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/longest-common-prefix
@Language: Python
@Datetime: 16-02-28 05:46
'''

class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        if strs is None or len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
            
        minLen = min([len(i) for i in strs])
        
        if minLen == 0:
            return ""
            
        for i in xrange(minLen+1):
            if i == minLen:
                return strs[0][:minLen]
            
            tmp = strs[0][i]
            for j in xrange(1, len(strs)):
                if strs[j][i] != tmp:
                    return strs[j][:i]
                    
                