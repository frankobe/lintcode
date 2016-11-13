# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/add-two-numbers
@Language: Python
@Datetime: 16-11-02 18:06
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        # write your code here
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        p1, p2 = ListNode(0), ListNode(0)
        p1.next = l1
        p2.next = l2
        addition = 0
        newHead = None
        dummy = None
        while not (p1.next is None and p2.next is None and addition == 0):
            val = addition
            if p1.next is not None:
                val += p1.next.val 
                p1 = p1.next
                
            if p2.next is not None:
                val += p2.next.val
                p2 = p2.next
                
            if val >= 10:
                addition = 1
                val = val - 10
            else:
                addition = 0
            
            node = ListNode(val)
            if dummy is None:
                dummy = node
            else:
                dummy.next = node
                dummy = node
                
            if newHead is None:
                newHead = node
                
        return newHead
        
        
        
        
            