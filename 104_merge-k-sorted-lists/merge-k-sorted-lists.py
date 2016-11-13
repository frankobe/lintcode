# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/merge-k-sorted-lists
@Language: Python
@Datetime: 15-09-02 05:27
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    
    def mergeTwo(self, h1, h2):
        
        if h1 is None:
            return h2
        if h2 is None:
            return h1
            
        dummy = ListNode(0)
        tail  = dummy 
        
        while h1 is not None and h2 is not None:
            if h1.val > h2.val:
                tail.next = h2
                h2 = h2.next
            else:
                tail.next = h1
                h1 = h1.next
                
            tail = tail.next
        
        if h1 is not None:
            tail.next = h1
        
        if h2 is not None:
            tail.next = h2
            
        return dummy.next
            
    def mergeHelper(self, lists, start, end):
        if start == end:
            return lists[start]
        
        middle = (start + end)/2
        left = self.mergeHelper(lists, start, middle)
        right = self.mergeHelper(lists, middle+1,end)
        return self.mergeTwo(left, right)
        
    def mergeKLists(self, lists):
        # write your code here
        if len(lists) == 0:
            return None
        
        return self.mergeHelper(lists, 0, len(lists)-1)
            
        
        


