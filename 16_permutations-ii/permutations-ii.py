# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/permutations-ii
@Language: Python
@Datetime: 15-06-23 18:34
'''

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    
    def permuteHelper(self, nums, result, tmpList, visited):
        
        numsLen = len(nums)
        if len(tmpList) == numsLen:
            result.append(list(tmpList))
            return
        
        for i in range(0, numsLen):
            if visited[i] == 1 or (i >0 and nums[i] == nums[i - 1] and visited[i - 1] == 1):
                continue
            
            visited[i] = 1
            tmpList.append(nums[i])
            self.permuteHelper(nums, result, tmpList, list(visited))
            tmpList.pop()
            visited[i] = 0
            
        
    def permuteUnique(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return []
            
        result = []
        nums.sort()
        visited = [0]*len(nums)
        self.permuteHelper(nums, result, [], visited)
        return result

