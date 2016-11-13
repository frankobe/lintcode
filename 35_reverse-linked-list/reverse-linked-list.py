# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/reverse-linked-list
@Language: Python
@Datetime: 15-08-24 02:16
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
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        
        if head is None:
            return None
        
        start = None
        
        while head is not None:
            tmp = head.next
            head.next = start
            start = head
            head = tmp
            
        return start
            
