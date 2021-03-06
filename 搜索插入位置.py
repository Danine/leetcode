'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
示例 1:                 示例 2:                 示例 3:
输入: [1,3,5,6], 5      输入: [1,3,5,6], 2      输入: [1,3,5,6], 7
输出: 2                 输出: 1                 输出: 4
'''
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 遍历nums，如果target小于等于nums，就插在这个地方
        if target > nums[len(nums)-1]:
            return len(nums)
        for i in range(len(nums)):
            if target <= nums[i]:
                return i

nums = [1,3,5,6]; target = 7
t = Solution()
print(t.searchInsert(nums,target))