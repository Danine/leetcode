class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                del nums[i+1]
        return len(nums)

nums = [0,0,1,2,3,3,4,5,5,5,5,5,5,5,5]
t = Solution()
print(t.removeDuplicates(nums))