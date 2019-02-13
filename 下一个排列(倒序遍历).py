'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。
以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
1234 → 1243 → 1324 → 1342 → 1423 → 1432
从数组倒着查找，找到nums[i-1] 比nums[i]小的时候，就将nums[i-1]跟nums[i]到nums[nums.length - 1]当中
找到一个最小的比nums[i-1]大的元素交换。交换后，再把nums[i]到nums[nums.length-1]排序
'''
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
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
                return nums

nums = [1,2,3,4]
t = Solution()
print(t.nextPermutation(nums))