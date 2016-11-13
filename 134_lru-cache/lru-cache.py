# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/lru-cache
@Language: Python
@Datetime: 16-10-27 18:04
'''

from collections import deque
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.htable = {}
        self.deque = deque()
        self.capacity = capacity
        
    # @return an integer
    def get(self, key):
        # write your code here
        if key not in self.htable:
            return -1
        
        self.deque.remove(key)
        self.deque.append(key)
        return self.htable[key]
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if key in self.htable:
            self.htable[key] = value
            self.deque.remove(key)
            self.deque.append(key)
        elif len(self.htable) < self.capacity:
            self.htable[key] = value
            self.deque.append(key)
        else:
            oldK = self.deque.popleft()
            self.htable.pop(oldK)
            self.htable[key]=value
            self.deque.append(key)
        
        # print self.deque, self.htable, self.capacity
            