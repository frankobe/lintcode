# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/search-range-in-binary-search-tree
@Language: Python
@Datetime: 15-07-20 18:34
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """
    def searchRangeHelper(self, root, k1, k2, result):
        if root is None:
            return
        
        if root.val > k1:
            self.searchRangeHelper(root.left, k1, k2, result)
            
        if root.val >= k1 and root.val <= k2:
            result.append(root.val)
            # self.searchRangeHelper(root.left, k1, k2, result)
            # self.searchRangeHelper(root.right, k1, k2, result)
            
        if root.val < k2:
            self.searchRangeHelper(root.right, k1, k2, result)
        
    def searchRange(self, root, k1, k2):
        # write your code here
        result = []
        self.searchRangeHelper(root, k1, k2, result)
        result.sort()
        return result