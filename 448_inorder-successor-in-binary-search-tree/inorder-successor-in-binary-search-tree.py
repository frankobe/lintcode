# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/inorder-successor-in-binary-search-tree
@Language: Python
@Datetime: 15-10-05 00:52
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        
        #find p, save direct parent
        head = root
        directParent = None
        while head is not None and head.val != p.val:
            if head.val > p.val:
                directParent = head
                head = head.left
            else:
                head = head.right
        
        # cant find p
        if head is None:
            return None
        
        if head.right is None:
            return directParent
            
        #find smallest in right childrens
        smallestRightChild = p.right
        while smallestRightChild.left is not None:
            smallestRightChild = smallestRightChild.left
            
        return smallestRightChild


        