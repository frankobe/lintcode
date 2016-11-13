# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-sorted-list
@Language: Python
@Datetime: 15-08-24 01:39
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
        
        if head is None:  
            return head
        
        node = head
        while node.next is not None:
            tmp = node.next
            if node.val == tmp.val:
                node.next = tmp.next
    
            else:
                node = node.next
            
        return head
