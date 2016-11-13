# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/intersection-of-two-linked-lists
@Language: Python
@Datetime: 16-10-25 00:44
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        # Write your code here
        
        la, lb = 0, 0
        pa, pb = headA, headB
        
        while pa is not None:
            la += 1
            pa = pa.next
        
        while pb is not None:
            lb += 1
            pb = pb.next
        
        pa, pb = headA, headB
        
        if la > lb:
            for i in xrange(la-lb):
                if pa is not None:
                    pa = pa.next
                else:
                    return None
        else:
            for i in xrange(lb-la):
                if pb is not None:
                    pb = pb.next
                else:
                    return None
        
        
        while pa is not None and pb is not None:
            if pa == pb:
                return pa
            else:
                pa = pa.next
                pb = pb.next
        
        return None
        
        