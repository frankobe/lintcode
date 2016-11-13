# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/rehashing
@Language: Python
@Datetime: 15-10-06 06:49
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
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        if hashTable is None or len(hashTable) == 0:
            return None
        
        oriSize = len(hashTable)
        doubleSize = oriSize * 2
        
        result = [None] * doubleSize
        
        for listNode in hashTable:
            tmp = listNode
            while tmp is not None:
                newIdx = tmp.val % doubleSize
                if result[newIdx] is None:
                    result[newIdx] = ListNode(tmp.val)
                else:
                    dummy = result[newIdx] 
                    while dummy.next is not None:
                        dummy = dummy.next
                    dummy.next = ListNode(tmp.val)
                
                tmp = tmp.next
                    
        return result