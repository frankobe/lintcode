# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/partition-list
@Language: Python
@Datetime: 15-08-24 06:34
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
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        if head is None:
            return None
            
        left = ListNode(0)
        right = ListNode(0)
        leftHead, rightHead = left, right 
        
        while head is not None:
            if head.val < x:
                left.next = head
                left = head
            else:
                right.next = head
                right = head
            
            head = head.next
            
        right.next = None
        left.next = rightHead.next
        return leftHead.next