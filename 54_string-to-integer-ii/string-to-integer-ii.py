# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/string-to-integer-ii
@Language: Python
@Datetime: 16-02-28 09:55
'''

class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str):
        # write your code here
        if str is None or len(str) == 0:
            return 0
        
        result = 0
        neg = False
        newStr = self.extractNum(str)
        if newStr is None:
            return 0
        
        if '.' in newStr:
            newStr = newStr[:newStr.index('.')]
            
        if '-' in newStr:
            if newStr[0] == '-':
                neg = True
                newStr = newStr[1:]
            else:
                return 0
                
        if '+' in newStr:
            if newStr[0] == '+':
                neg = False
                newStr = newStr[1:]
            else:
                return 0
        
        for i in xrange(len(newStr)):
            power = len(newStr) - 1 - i
            digit = self.digit(newStr[i])
            if digit == -1:
                break
            else:
                result += digit*10**power
            
        if neg:
            result = -result
        
        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        
        return result
            
            
    def extractNum(self, str):
        start, end = -1, -1
        for i in xrange(len(str)):
            if start != -1 and end == -1:
                if not self.isDigitOnly(str[i]):
                    end = i
                    return str[start:end]
                    
            if start == -1:
                if self.isDigit(str[i]):
                    start = i
            
        if start != -1 and end == -1:
            return str[start:]
        
        else :
            return None

    def digit(self, str):
        if str == '0':
            return 0
        if str == '1':
            return 1
        if str == '2':
            return 2
        if str == '3':
            return 3
        if str == '4':
            return 4
        if str == '5':
            return 5
        if str == '6':
            return 6
        if str == '7':
            return 7
        if str == '8':
            return 8
        if str == '9':
            return 9
        return -1
        
    def isDigitOnly(self, str):
        if str == '0':
            return True
        if str == '1':
            return True
        if str == '2':
            return True
        if str == '3':
            return True
        if str == '4':
            return True
        if str == '5':
            return True
        if str == '6':
            return True
        if str == '7':
            return True
        if str == '8':
            return True
        if str == '9':
            return True
            
        return False
        
    def isDigit(self, str):
        if str == '0':
            return True
        if str == '1':
            return True
        if str == '2':
            return True
        if str == '3':
            return True
        if str == '4':
            return True
        if str == '5':
            return True
        if str == '6':
            return True
        if str == '7':
            return True
        if str == '8':
            return True
        if str == '9':
            return True
        if str == '+':
            return True
        if str == '-':
            return True
        if str == '.':
            return True
            
        return False


        