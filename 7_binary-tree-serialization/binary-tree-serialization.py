# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/binary-tree-serialization
@Language: Python
@Datetime: 16-02-17 19:59
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        if root is None or root.val == '#':
            return []
        
        q = [root]
        # result = [root.val]
        result = str(root.val)
        while len(q) > 0:
            node = q.pop(0)
            result = result+','
            if node.left:
                # result.append(node.left.val)
                result = result + str(node.left.val)
                q.append(node.left)
            else:
                # result.append('#')
                result = result + '#'
                
            result = result+','    
            if node.right:
                # result.append(node.right.val)
                result = result + str(node.right.val)
                q.append(node.right)
            else:
                # result.append('#')
                result = result + '#'
        
        return result
    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        if data is None or len(data) == 0:
            return None

        if len(data) == 1 and data[0] == '#':
            return None

        array = data.split(',')
        root = TreeNode(array[0])
        parentList = [root]
        currentParentIdx = 0
        isLeftChild = True
        for i in xrange(1, len(array)):
            parent = parentList[currentParentIdx]
            tmpNode = None
            if array[i] != '#':
                tmpNode = TreeNode(int(array[i]))
                parentList.append(tmpNode)
        
            if isLeftChild:
                parent.left = tmpNode
            else:
                parent.right = tmpNode
                currentParentIdx = currentParentIdx + 1
            isLeftChild = not isLeftChild
        return root