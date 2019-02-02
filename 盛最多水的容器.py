'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai)。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。
示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leng = len(height)
        maxc = 0
        # #暴力法
        # for i in range(leng-1):
        #     for j in range(1,leng):
        #         sq = min(height[i],height[j]) * (j-i)
        #         if sq > maxc:
        #             maxc = sq
        # return maxc

        # #与最大值比较
        # i = 0; j = leng - 1
        # while j - i > 0:
        #     sq = min(height[i],height[j]) * (j-i)
        #     if sq > maxc:
        #         maxc = sq
        #     if height[i] <= height[j]:
        #         i += 1
        #     else:
        #         j -= 1
        # return maxc

        #加入列表找最大值
        i = 0; j = leng - 1; s = []
        while j - i > 0:
            sq = min(height[i],height[j]) * (j-i)
            s.append(sq)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        maxc = max(s)
        return maxc
height = [1,8,6,2,5,4,8,3]
t = Solution()
print(t.maxArea(height))