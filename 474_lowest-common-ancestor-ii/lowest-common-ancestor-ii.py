# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/lowest-common-ancestor-ii
@Language: Python
@Datetime: 16-02-16 02:06
'''

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
class Solution:
    """
    @param root: The root of the tree
    @param A and B: Two node in the tree
    @return: The lowest common ancestor of A and B
    """ 
    # sol 1: without parent
    # def lowestCommonAncestorII(self, root, A, B):
    #     # Write your code here
    #     if root is None or root.val == A.val or root.val == B.val:
    #         return root
            
    #     left = self.lowestCommonAncestorII(root.left, A, B)
    #     right = self.lowestCommonAncestorII(root.right, A, B)
        
    #     if left is not None and right is None:
    #         return left
        
    #     if right is not None and left is None:
    #         return right
            
    #     if left is not None and right is not None:
    #         return root
        
    #     return None
    
    # sol 2: simly contain
    # def lowestCommonAncestorII(self, root, A, B):
        
    #     if root is None or A is None or B is None:
    #         return None
            
    #     nodeList = []
        
    #     nextA = A
    #     nextB = B
    #     while nextA or nextB:
    #         if nextA:
    #             if nextA in nodeList:
    #                 return nextA
    #             else:
    #                 nodeList.append(nextA)
    #                 nextA = nextA.parent
            
    #         if nextB:
    #             if nextB in nodeList:
    #                 return nextB
    #             else:
    #                 nodeList.append(nextB)
    #                 nextB = nextB.parent
        
    #     return root
            
    # sol 3: minize height    
    def lowestCommonAncestorII(self, root, A, B):
            
        if root is None or A is None or B is None:
            return None
            
        hA, hB = 0, 0
        nextA, nextB = A, B
        while nextA or nextB:
            if nextA:
                hA = hA + 1
                nextA = nextA.parent
        
            if nextB:
                hB = hB + 1
                nextB = nextB.parent
                
        nextA, nextB = A, B
        
        if hA > hB:
            hA, hB = hB, hA
            nextA, nextB = B, A
        
        hd = hB - hA
        
        while hd > 0:
            nextB = nextB.parent
            hd = hd - 1
            
        while nextA and nextB:
            if nextA == nextB:
                return nextA
            else:
                nextA = nextA.parent
                nextB = nextB.parent
            
        return None
            
            