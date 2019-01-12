'''
给定一个 haystack 字符串和一个 needle 字符串，
在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1。
示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1
'''
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 注释里的方法在执行最后一个样例时超时，抖机灵的3行却没有……怀疑自己的智商
        # h = list(haystack); n = list(needle)
        # if n == []:
        #     return 0
        # for i in range(len(h)):
        #     if h[i] == n[0]:
        #         for j in range(len(n)):
        #             k = i + j
        #             if k < len(h) and n[j] == h[k]:
        #                 if j+1 == len(n):
        #                     return i
        #             else:
        #                 break
        # return -1
        if needle in haystack:
            return haystack.index(needle)
        return -1

haystack = "aaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaba"
needle = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
t = Solution()
print(t.strStr(haystack,needle))