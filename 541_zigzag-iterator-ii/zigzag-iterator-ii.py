# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/zigzag-iterator-ii
@Language: Python
@Datetime: 16-11-01 16:30
'''

class ZigzagIterator2:

    # @param {int[][]} a list of 1d vectors
    def __init__(self, vecs):
        # initialize your data structure here
        self.vecs = vecs
        self.p = 0

    def next(self):
        # Write your code here
        while len(self.vecs[self.p]) == 0:
            self.p = (self.p + 1)%len(self.vecs)
        
        p = self.p
        self.p = (self.p + 1)%len(self.vecs)
        return self.vecs[p].pop(0)

    def hasNext(self):
        # Write your code here
        for v in self.vecs:
            if len(v) > 0:
                return True
        
        return False

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result