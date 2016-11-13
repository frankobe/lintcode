# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/zigzag-iterator
@Language: Python
@Datetime: 16-11-01 16:30
'''

class ZigzagIterator:

    # @param {int[]} v1 v2 two 1d vectors
    def __init__(self, v1, v2):
        # initialize your data structure here
        self.v1 = v1
        self.v2 = v2
        self.nextP = 1

    def next(self):
        # Write your code here
        if self.nextP == 1:
            self.nextP = 2
            if len(self.v1) > 0:
                return self.v1.pop(0)
            else:
                return self.v2.pop(0)
            
        else:
            self.nextP = 1
            if len(self.v2) > 0:
                return self.v2.pop(0)
            else:
                return self.v1.pop(0)
            

    def hasNext(self):
        # Write your code here
        if len(self.v1) == 0 and len(self.v2) == 0:
            return False
        else:
            return True

# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result
