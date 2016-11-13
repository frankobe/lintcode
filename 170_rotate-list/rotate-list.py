# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/rotate-list
@Language: Python
@Datetime: 16-10-25 01:04
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        if head is None or k <= 0:
            return head
        
        l = 0
        p = head
        while p is not None:
            l += 1
            p = p.next
        
        k = k%l
        if k==0:
            return head
        
        p = head
        for i in xrange(l - k - 1):
            p = p.next
            
        newHead = p.next
        p.next = None
        p = newHead
        
        for i in xrange(k-1):
            p = p.next
        
        p.next = head
        
        return newHead