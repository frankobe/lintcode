# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/binary-tree-level-order-traversal
@Language: Python
@Datetime: 15-09-06 18:57
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
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []
        
        result = []
        levelQueue = []
        
        levelQueue.append(root)
        
        while len(levelQueue) != 0:
            levelList = []
            for node in list(levelQueue):
                levelList.append(node.val)
                levelQueue.remove(node)
                
                if node.left is not None:
                    levelQueue.append(node.left)
                
                if node.right is not None:
                    levelQueue.append(node.right)
                    
            result.append(list(levelList))
            
        
        return result
        
        
        # while levelQueue:
        #     levelVal = []
        #     for i in range(len(levelQueue)):
        #         node = levelQueue[0]
        #         levelQueue.pop(0)
        #         levelVal.append(node.val)
                
        #         if node.left is not None:
        #             levelQueue.append(node.left)
                    
        #         if node.right is not None:
        #             levelQueue.append(node.right)
                    
        #     result.append(list(levelVal))
            
        
        return result