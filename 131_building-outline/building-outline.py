# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/building-outline
@Language: Python
@Datetime: 16-04-20 22:48
'''

class HashHeap:
    def __init__(self):
        self.heap = []
        self.hash = {}
        self.size = 0
    # index
    def _swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
        
        self.hash[self.heap[a][1]] = a
        self.hash[self.heap[b][1]] = b
    # index
    def _siftup(self, index):
        t = index
        while (t-1)/2 >= 0:
            if self.heap[t][0] > self.heap[(t-1)/2][0]:
                self._swap(t, (t-1)/2)
                t = (t-1)/2
                continue
            break
        return t
    # index
    def _siftdown(self, index):
        t = index
        while t*2+1 < self.size:
            child_index = t*2 + 1
            child_height = self.heap[child_index][0]
            
            if t*2 + 2 < self.size and child_height < self.heap[t*2+2][0]:
                child_index = t*2 + 2
                child_height = self.heap[child_index][0]
                
            if self.heap[t][0] < child_height:
                self._swap(t, child_index)
                t = child_index
                continue
            break
        return t


    def add(self, key, value):        
        self.size += 1
        self.hash[key] = self.size-1
        self.heap.append((value, key))
        self._siftup(self.size-1)

    def remove(self, key):
        index = self.hash[key]
        self._swap(index, self.size -1)
        del self.hash[key]
        self.heap.pop()
        self.size -= 1
        if index < self.size:
            self._siftup(self._siftdown(index))


    def hasKey(self, key):
        return key in self.hash

    def max(self):
        return self.heap[0][0] if len(self.heap) != 0 else 0

class Solution:
    # @param buildings: A list of lists of integers
    # @return: A list of lists of integers
    def buildingOutline(self, buildings):
        # write your code here
        if buildings is None:
            return None
        
        begins = [(b[0], b[2], index) for index, b in enumerate(buildings)]
        ends = [(b[1], b[2], index) for index, b in enumerate(buildings)]
        heights = sorted(begins + ends, key=lambda x: x[0])

        # print heights

        hashheap = HashHeap()
        y = {}
        for x, height, index in heights:
            if hashheap.hasKey(index):
                hashheap.remove(index)
            else:
                hashheap.add(index, height)
            y[x] = hashheap.max()


        y = sorted(y.iteritems(), key=lambda x: x[0])
        
        result = []
        start, end = None, None
        for (i, h) in y:
            if start is None:
                start = (i, h)
                continue

            end = (i,h)
            if end[1] == start[1]:
                continue

            result.append([start[0], end[0], start[1]])
            if end[1] == 0:
                start = None
            else:
                start = end
        
        return result
