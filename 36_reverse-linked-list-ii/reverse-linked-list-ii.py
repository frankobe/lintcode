# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/reverse-linked-list-ii
@Language: Python
@Datetime: 16-10-21 21:15
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
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        # if head is None:
        #     return None
            
        # dummy = ListNode(0)
        # dummy.next = head
        
        # preM = dummy
        # for i in range(1, m):
        #     preM = preM.next

        # mNode = preM.next
        # start = mNode
        # iterator = start.next
        
        # for i in range(n-m):
        #     if iterator is None:
        #         return None
                
        #     tmp = iterator.next
        #     iterator.next = start
        #     start = iterator
        #     iterator = tmp
            
        # preM.next = start
        # mNode.next = iterator
        
        # return dummy.next
        
        if head is None or m > n:
            return None
        
        dummy = ListNode(0, head)
        preM = dummy
        
        for i in xrange(m-1):
            preM = preM.next
            
        start = preM.next
        end = preM.next
        iterator = start.next
        # print start.val, end.val, iterator.val
        for i in xrange(n-m):
            tmp = iterator.next
            iterator.next = end
            end = iterator
            iterator = tmp
        
        # print end.val, iterator.val
        preM.next = end
        start.next = iterator
        
        return dummy.next
            
        
            
            
            
        

