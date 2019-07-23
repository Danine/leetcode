'''
给定一个没有重复数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
1234
1243
1324
1342
1423
1432

'''
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        allnums = []
        for i in range(length-1,-1,-1): #倒序遍历
            if nums[i] > nums[i-1]:
                mark = i
                more = nums[i]
                for j in range(i,length):   #查找最小的比nums[i-1]大的元素
                    if nums[j] > nums[i-1] and nums[j] < more:
                        more = nums[j]
                        mark = j
                temp = more
                nums[mark] = nums[i-1]
                nums[i-1] = temp
                sort = nums[i:length]
                sort.sort()
                for i in range(len(sort)):
                    nums.pop()
                nums.extend(sort)
                allnums.extend(nums)
        return allnums

nums = [1,2,3,4]
t = Solution()
print(t.permute(nums))