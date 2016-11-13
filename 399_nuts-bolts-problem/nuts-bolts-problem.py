# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/nuts-bolts-problem
@Language: Python
@Datetime: 16-04-30 06:08
'''

# class Comparator:
#     def cmp(self, a, b)
# You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
# if "a" is bigger than "b", it will return 1, else if they are equal,
# it will return 0, else if "a" is smaller than "b", it will return -1.
# When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        # write your code here
    
        n = len(nuts)
        
        self.quicksort(0, n-1, nuts, bolts, compare)
    
    def quicksort(self, lo, hi, nuts, bolts, compare):
        if lo < hi:
            b_p = self.partition(nuts[lo], lo, hi, bolts, compare)
            n_p = self.partition(bolts[b_p], lo, hi, nuts, compare)
            self.quicksort(lo, b_p-1, nuts, bolts, compare)
            self.quicksort(b_p+1, hi, nuts, bolts, compare)
            
    def partition(self, pivot, lo, hi, items, compare):
        left, right = lo, hi
        while left < right:
            while compare.cmp(pivot, items[left]) == 1 or \
                compare.cmp(items[left], pivot) == -1:
                left +=1
            while compare.cmp(pivot, items[right]) == -1 or \
                compare.cmp(items[right], pivot) == 1:
                right -=1
            
            swap(left, right, items)
        return left
    
def swap(a, b, array):
    array[a], array[b] = array[b], array[a]