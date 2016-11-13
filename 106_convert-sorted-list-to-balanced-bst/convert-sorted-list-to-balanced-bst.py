# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/convert-sorted-list-to-balanced-bst
@Language: Python
@Datetime: 15-09-02 21:17
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def bstHelper(self, head, length):
        if length <= 0:
            return None
            
        mid = length/2
        midListNode = ListNode(0)
        midListNode.next = head
        for i in xrange(mid+1):
            midListNode = midListNode.next
        
        left = self.bstHelper(head, length/2)
        right = self.bstHelper(midListNode.next, length - length/2 - 1)
        
        rootNode = TreeNode(midListNode.val)
        rootNode.left = left
        rootNode.right = right
        return rootNode
        
        
    def listLength(self, head):
        count = 0
        tmp = head
        while tmp is not None:
            count = count +1
            tmp = tmp.next
            
        return count
        
    def sortedListToBST(self, head):
        # write your code here
        if head is None:
            return None
            
        length = self.listLength(head)
        return self.bstHelper(head, length)
