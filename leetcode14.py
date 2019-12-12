# -*- encoding = utf-8 -*-
# Leetcode-14
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 首先先排序，时间复杂度为NLogN,之后再用双指针的方法，慢慢逼近target
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        ans = nums[0]+ nums[1] + nums[2]
        def abs(x):
            return x if x >= 0 else -x
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if abs(target - sum) < abs(target - ans):
                    ans = sum
                if sum > target:
                    end -= 1
                elif sum < target:
                    start += 1
                else:
                    return ans
        return ans

if __name__ == '__main__':
    nums = [-3,-2,-5,3,-4]
    target = -1
    print(Solution().threeSumClosest(nums,target))

