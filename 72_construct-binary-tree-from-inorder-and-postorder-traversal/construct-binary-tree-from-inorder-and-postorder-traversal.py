# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/construct-binary-tree-from-inorder-and-postorder-traversal
@Language: Python
@Datetime: 16-03-07 00:55
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
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        if inorder is None or len(inorder) == 0 or postorder is None or len(postorder) == 0:
            return None
        
        if len(inorder) != len(postorder):
            return None
        
        
        root = TreeNode(postorder[-1])
        rootIdx = inorder.index(root.val)
        
        root.left = self.buildTree(inorder[:rootIdx], postorder[:rootIdx])
        root.right = self.buildTree(inorder[rootIdx+1:], postorder[rootIdx:len(postorder)-1])
        
        return root