# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-sorted-list-ii
@Language: Python
@Datetime: 16-10-20 22:08
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
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        # if head is None:
        #     return None
        
        # dummy = ListNode(0)
        # dummy.next = head
        
        # start = dummy
        
        # while start.next is not None and start.next.next is not None:
        #     if start.next.val == start.next.next.val:
        #         valueHolder = start.next.val
        #         while start.next is not None and start.next.val == valueHolder:
        #             start.next = start.next.next
                    
        #     else:
        #         start = start.next
            
        # return dummy.next
        
        if head is None:
            return None
        
        dummy = ListNode(0, head)
        
        now = dummy
        
        while now.next is not None and now.next.next is not None:
            if now.next.val == now.next.next.val:
                value = now.next.val
                while now.next is not None and now.next.val == value:
                    now.next = now.next.next
            else:
                now = now.next
        
        return dummy.next
            
                
            
        
            
        