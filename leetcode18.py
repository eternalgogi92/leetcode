# -*- encoding = utf-8 -*-
# Leetcode-14
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组
# 参考三值求和用的双指针法，这里固定住两个数，然后移动start和end，注意判断answer是否会重复。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/4sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        nums = sorted(nums)
        length = len(nums)
        for i in range(length-2):
            for j in range(i+1,length-1):
                start = j + 1
                end =  length - 1
                while start < end:
                    sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if sum < target:
                        start += 1
                    elif sum > target:
                        end -= 1
                    else:
                        if [nums[i],nums[j],nums[start],nums[end]] not in ans:
                            ans.append([nums[i],nums[j],nums[start],nums[end]])
                        start += 1
                        end -= 1
        return ans

if __name__ == '__main__':
    # nums = [1, 0, -1, 0, -2, 2]
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0
    ans = Solution().fourSum(nums,target)
    print(ans)


