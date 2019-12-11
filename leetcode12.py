# -*- encoding = utf-8 -*-
# Leetcode-12
# I:1 V:5 X:10 L:50 C:100 D:500 M:1000
# 参考了下，和leetcode上给出的贪心算法差不多，不过上面先列出了900,500,90,50,9,5对应的阿拉伯数字解，总体思路差不多

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        digit = num // 1000
        left = num % 1000
        for i in range(digit):
            res += 'M' # the num <= 3999
        digit = left // 100
        left = left % 100
        if digit == 9:
            res += 'CM'
        elif digit ==4:
            res += 'CD'
        elif digit in range(5,9):
            res += 'D' + 'C' * (digit - 5)
        else:
            res += 'C' * digit
        digit = left // 10
        left = left % 10
        if digit == 9:
            res += 'XC'
        elif digit == 4:
            res += 'XL'
        elif digit in range(5,9):
            res += 'L' + 'X' * (digit -5)
        else:
            res += 'X' * digit
        digit = left
        if digit == 9:
            res += 'IX'
        elif digit == 4:
            res += 'IV'
        elif digit in range(5,9):
            res += 'V' + 'I' * (digit - 5)
        else:
            res += 'I' * digit
        return res

if __name__ == '__main__':
    nums = [1994]
    for num in nums:
        print(Solution().intToRoman(num))
