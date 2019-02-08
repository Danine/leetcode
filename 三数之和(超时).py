'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rt = []
        length = len(nums)
        #会超时
        for i in range(length-1):
            for j in range(i+1,length):
                c = 0 - nums[i] - nums[j]
                three = [nums[i],c,nums[j]]
                three.sort()
                temp = nums.copy()
                temp.pop(j); temp.pop(i)
                if c in temp and three not in rt:
                    rt.append(three)
        return rt

nums = [3,0,-2,-1,1,2]
t = Solution()
print(t.threeSum(nums))
