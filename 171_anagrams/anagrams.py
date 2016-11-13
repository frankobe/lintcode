# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/anagrams
@Language: Python
@Datetime: 16-02-28 04:09
'''

class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        
        if strs is None or len(strs) == 0:
            return []
            
        dict = {}
        result = []
        for word in strs:
            hash = self.hash(word)
            if hash in dict:
                dict[hash].append(word)
            else:
                dict[hash] = [word]
                
        for v in dict.values():
            if len(v) > 1:
                result.extend(v)
                
        return result

    def hash(self, word):
        result = [0]*26
        for i in xrange(len(word)):
            val = ord(word[i]) - ord('a')
            result[val] += 1
            
        hashStr = ''
        for i in xrange(len(result)):
            hashStr += str(result[i])
            
        return hashStr