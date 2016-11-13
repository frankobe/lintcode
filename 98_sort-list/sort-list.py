# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/sort-list
@Language: Python
@Datetime: 15-08-24 07:24
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
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    
    def findMiddle(self, head):
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
                
            tail = tail.next
        
        if l1 is None:
            tail.next = l2
        else:
            tail.next = l1
        
        return dummy.next
        
    def sortList(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
            
        middleNode = self.findMiddle(head)
        right = self.sortList(middleNode.next)
        middleNode.next = None
        left = self.sortList(head)
        
        return self.merge(left, right)