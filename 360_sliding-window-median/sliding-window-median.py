# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/sliding-window-median
@Language: Python
@Datetime: 16-04-21 23:13
'''

class HashHeap:
    def __init__(self, isMinHeap=True):
        self.heap = []
        self.hash = {}
        self.isMinHeap = isMinHeap
        self.size = 0

    def add(self, key, value):        
        self.size += 1
        self.hash[key] = self.size-1
        self.heap.append((value, key))
        self._siftup(self.size-1)

    def pop(self):
        if self.size > 0:
            val = self.heap[0]
            self.remove(val[1])
            return val
        else:
            return None

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

    def peak(self):
        return self.heap[0][0] if len(self.heap) != 0 else 0
        
    # index
    def _swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
        
        self.hash[self.heap[a][1]] = a
        self.hash[self.heap[b][1]] = b
        
    # index
    def _siftup(self, index):
        t = index
        while (t-1)/2 >= 0:
            if self.isMinHeap:
                if self.heap[t][0] < self.heap[(t-1)/2][0]:
                    self._swap(t, (t-1)/2)
                    t = (t-1)/2
                    continue
                break
            else:
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
            
            if self.isMinHeap:
                if t*2 + 2 < self.size and child_height > self.heap[t*2+2][0]:
                    child_index = t*2 + 2
                    child_height = self.heap[child_index][0]
                    
                if self.heap[t][0] > child_height:
                    self._swap(t, child_index)
                    t = child_index
                    continue
                break
            else:
                if t*2 + 2 < self.size and child_height < self.heap[t*2+2][0]:
                    child_index = t*2 + 2
                    child_height = self.heap[child_index][0]
                    
                if self.heap[t][0] < child_height:
                    self._swap(t, child_index)
                    t = child_index
                    continue
                break             
        return t

class Solution():
     def medianSlidingWindow(self, nums, k):

        
        if nums is None or len(nums) < k or len(nums) == 0 or k == 0:
            return []

        minHeap = HashHeap(True)
        maxHeap = HashHeap(False)
        median = None

        init = []
        for i in xrange(k):
            init.append((i, nums[i]))
        
        init = sorted(init, key=lambda x:x[1])
        
        mid = (k-1)/2
        for i in xrange(mid+1):
            maxHeap.add(init[i][0], init[i][1])

        for i in xrange(mid+1, k):
            minHeap.add(init[i][0], init[i][1])

        result = [init[mid][1]]
        for i in xrange(k,len(nums)):
            if minHeap.hasKey(i-k):
                minHeap.remove(i-k)
            elif maxHeap.hasKey(i-k):
                maxHeap.remove(i-k)

            minHeap.add(i, nums[i])
            if minHeap.peak() < maxHeap.peak():
                # swap
                minVal, minKey = minHeap.pop()
                maxVal, maxKey = maxHeap.pop()
                minHeap.add(maxKey, maxVal)
                maxHeap.add(minKey, minVal)

            if minHeap.size > maxHeap.size :
                median, key = minHeap.pop()
                result.append(median)
                maxHeap.add(key, median)
                continue

            else:
                result.append(maxHeap.peak())
                continue

        return result







        