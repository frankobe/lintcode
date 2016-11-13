# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/word-ladder
@Language: Python
@Datetime: 15-09-10 00:43
'''

from string import ascii_lowercase

class Solution:
    def replace(self, word, index, newChar):
        newWord = word[:index]+newChar+word[(index+1):]
        return newWord
            
    def ladderLength(self, start, end, dict):
        # write your code here
        levelSet ={start} 
        level = 1
        size = len(start)
        while level:
            level += 1
            for word in set(levelSet):
                for i in xrange(size):
                    for c in ascii_lowercase:
                        if c != word[i]:
                            nextWord = word[:i]+c+word[i+1:]
                            if nextWord == end:
                                return level
                            
                            if nextWord in dict:
                                levelSet.add(nextWord)
                                dict.remove(nextWord)
                            
                levelSet.remove(word)        
                    
        return 0
                
    
