# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/reorder-list
@Language: Python
@Datetime: 15-08-25 18:14
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
    @return: nothing
    """
    def findMiddle(self, head):
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
    def reverse(self, head):
        if head is None or head.next is None:
            return head
            
        newHead = None
        while head is not None:
            tmp = head.next
            head.next = newHead
            newHead = head
            head = tmp
        return newHead
    
    def merge(self, head, tail):
        # dummy = ListNode(0)
        # index = 0
        while head is not None and tail is not None:
            headNext = head.next
            tailNext = tail.next
            
            head.next = tail
            tail.next = headNext
            
            head = headNext
            tail = tailNext
            # if index %2 ==0:
            #     dummy.next = head
            #     head = head.next
            # else:
            #     dummy.next = tail
            #     tail = tail.next
                
            # dummy = dummy.next
            # index = index + 1


        # if head is not None:
        #     dummy.next = head
        # if tail is not None:
            # dummy.next = tail
    
    def reorderList(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        
        middle = self.findMiddle(head)
        tail = self.reverse(middle.next)
        middle.next = None
        
        self.merge(head, tail)
        
        return head
    
        
        

