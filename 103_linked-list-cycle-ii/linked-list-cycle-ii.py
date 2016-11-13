# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/linked-list-cycle-ii
@Language: Python
@Datetime: 15-09-04 03:30
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
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """

    def detectCycle(self, head):
        # write your code here
        if head is None:
            return None
        
        fast, slow = head, head
        
        while fast is not None and fast.next is not None:

            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                # hv link
                fast = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                
                return slow
            
        return None
        
        
        

