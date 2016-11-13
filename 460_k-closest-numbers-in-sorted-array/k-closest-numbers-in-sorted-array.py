# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/k-closest-numbers-in-sorted-array
@Language: Python
@Datetime: 16-02-04 06:00
'''

class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @param {int} k a non-negative integer
    # @return {int[]} an integer array
    def kClosestNumbers(self, A, target, k):
        # Write your code here
        if A is None or len(A) == 0 or k is None or k == 0:
            return []
        
        start, end = 0, len(A) -1 
        foundIndex = -1
        
        while start < end:
            mid = (start + end)/2
            if mid == start:
                break
            
            if A[mid] > target:
                end  = mid
            elif A[mid] < target:
                start = mid
            else:
                foundIndex = mid
                break
        
        result = []
        if foundIndex != -1:
            result.append(target)
            leftset = A[:foundIndex]
            rightset = A[(foundIndex+1):]
        else:
            leftset = A[:(start+1)]
            rightset = A[end:]

        leftIdx, rightIdx = -1, 0
        lenLeft, lenRight = len(leftset), len(rightset)
        while len(result) < k and len(result) < len(A):
            left, right = None, None  
            if -leftIdx <= lenLeft:
                left = leftset[leftIdx]
            
            if rightIdx < lenRight:
                right = rightset[rightIdx]
            
            if left is None and right is None:
                return result
            elif left is None:
                result.append(right)
                rightIdx = rightIdx + 1
            elif right is None:
                result.append(left)
                leftIdx = leftIdx - 1
            elif target - left > right - target:
                result.append(right)
                rightIdx = rightIdx + 1
            else:
                result.append(left)
                leftIdx = leftIdx - 1
        return result
            
        