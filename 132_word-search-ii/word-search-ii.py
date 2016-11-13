# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/word-search-ii
@Language: Python
@Datetime: 16-04-17 08:25
'''

class TrieNode:
    def __init__(self):
        self.isLeaf = False
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def push(self, word):
        if word == '':
            return 
        p = self.root
        for i in word:
            if i not in p.children:
                p.children[i] = TrieNode()
            p = p.children[i]
            
        p.isLeaf = True
            
    
class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def wordSearchII(self, board, words):
        # write your code here
        if words is None or len(words) == 0:
            return words
            
        if board is None:
            return []
            
        self.m = len(board)
        if self.m == 0:
            return []
            
        self.n = len(board[0])
        if self.n == 0:
            return []
            
        trie = Trie()
        
        for w in words:
            trie.push(w)
        
        self.direction = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]
        self.result = set()
        
        for i in xrange(self.m):
            for j in xrange(self.n):
                self.search(trie.root, board, i, j, '')
        
        return list(self.result)
            
    def search(self, node, board, i, j, word):
        char = board[i][j]
     
        if char not in node.children:
            return
        
        nextNode = node.children[char]
        
        if nextNode.isLeaf:
            self.result.add(word+char)
            
        board[i][j] = None
        for k in range(4):
            nx = i + self.direction[k][0]
            ny = j + self.direction[k][1]
            if nx < 0 or nx >= self.m or ny < 0 or ny >= self.n or board[nx][ny] is None:
                continue
            self.search(nextNode, board,nx, ny, word+char)
        
        board[i][j] = char