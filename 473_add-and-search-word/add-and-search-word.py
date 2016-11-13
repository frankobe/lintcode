# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/add-and-search-word
@Language: Python
@Datetime: 16-04-14 06:23
'''

class TrieNode:
    def __init__(self):
        self.isLeaf=False
        self.children=[None]*26
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0
    
    def insert(self, s):
        if len(s) == 0:
            return 0
        
        r = self.root
        i = 0
        while i < len(s):
            if r.children[ord(s[i])-ord('a')] is None:
                r.children[ord(s[i])-ord('a')] = TrieNode()
            r = r.children[ord(s[i])-ord('a')]
            i += 1
        r.isLeaf=True
        self.size += 1
        
    def search(self, s, p, i):
        if len(s) == i:
            return p.isLeaf
        
        
        if s[i] == '.':
            for j in xrange(26):
                if p.children[j] != None:
                    if self.search(s, p.children[j], i+1):
                        return True
        else:
            if p.children[ord(s[i]) - ord('a')] != None:
                if self.search(s, p.children[ord(s[i]) - ord('a')], i+1):
                    return True
        
        return False    

class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        # Write your code here
        self.trie = Trie()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        # Write your code here
        self.trie.insert(word)

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        # Write your code here
        return self.trie.search(word, self.trie.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")