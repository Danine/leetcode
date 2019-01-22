'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        maxc = nums[0]; sumc = 0; i = 0
        for i in range(length):
            if sumc > 0:
                sumc = sumc + nums[i]
            else:
                sumc = nums[i]
            if sumc > maxc:
                maxc = sumc
        return maxc

nums = [-2,-3]
t = Solution()
print(t.maxSubArray(nums))