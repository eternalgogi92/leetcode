# -*- encoding = utf-8 -*-
# Leetcode-11
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_area = 0
        start = 0
        end = n -1
        # 采用双指针解法，保证保留较长的那一边，然后寻找更高的较短的一边
        while start < end:
            cur_area = min(height[start],height[end]) * (end-start)
            max_area = max(max_area,cur_area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area



if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    res = Solution().maxArea(height)
    print(res)
