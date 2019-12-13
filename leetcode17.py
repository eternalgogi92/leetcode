# -*- encoding = utf-8 -*-
# Leetcode-14
#给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        for i in range(len(digits)):
            digit = int(digits[i])
            i = digit - 2
            if digit < 7:
                choice = alphas[i*3:i*3+3]
            elif digit == 7:
                choice = alphas[i*3:i*3+4]
            elif digit == 8:
                choice = alphas[i*3+1:i*3+4]
            elif digit == 9:
                choice = alphas[-4:]
            if len(res) == 0:
                for j in range(len(choice)):
                    res.append(choice[j])
            else:
                new_add = []
                for k in range(len(res)):
                    for j in range(len(choice)):
                        new_add.append(res[k]+choice[j])
                res = new_add
        return res

if __name__ == '__main__':
    digits = '8'
    print(Solution().letterCombinations(digits))
