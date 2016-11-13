# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/two-sum
@Language: Python
@Datetime: 16-05-02 06:22
'''

class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        
        # two pointer can't solve duplication
        # d = {}
        # for i in xrange(len(numbers)):
        #     d[numbers[i]] = {}
            
            
        # a = sorted(numbers)
        # # print a
        # start, end = 0, len(numbers) - 1
        
        # while start < end:
        #     s = a[start] + a[end]
        #     if s == target:
        #         return [min(d[a[start]], d[a[end]]), max(d[a[start]], d[a[end]])]
        #     elif s > target:
        #         end -= 1
        #     else:
        #         start += 1
        
        # return []
        
        # hash
        h = {}
        for i in xrange(len(numbers)):
            if target - numbers[i] in h:
                return [h[target - numbers[i]]+1, i+1]
            h[numbers[i]] = i
            
        return []