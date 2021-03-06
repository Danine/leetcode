'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
idea:set()是一个无序的不重复元素序列，类似于字典，不用遍历直接取元素
'''
class Solution:
	def twoSum(self, nums, target):
		k = len(nums)
		s = set(nums)
		for i in range(k):
			l = target - nums[i]
			if (l in s)and(nums.index(l) != i):
				return [i,nums.index(l)]

nums = [2, 7, 11, 15]; target = 18
t = Solution()
print(t.twoSum(nums,target))