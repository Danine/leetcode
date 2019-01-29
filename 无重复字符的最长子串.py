'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = list(s)
        length = len(s)
        maxc = 1
        ss = []
        # 思路：遍历字符串，在无重复的情况下将已经遍历的字符放到另一个数组中
        #       设置一个最大值与每一次遍历后的字符串进行比较
        #       若出现相同的，则将相同字符及之前的pop出去
        for i in range(length):
            if s[i] not in ss:
                ss.append(s[i])
            else:
                ss.append(s[i])
                for j in range(0,ss.index(s[i])+1):
                    ss.pop(0)
            if maxc < len(ss):
                maxc = len(ss)
        return maxc
        # l = 1
        # new = 0
        # maxc = 1
        # for i in range(1,length):
        #     if s[i] not in s[new:i]:
        #         l += 1
        #     else:
        #         new = s[0:i].index(s[i]) + 1
        #         s[new-1] = 0
        #         l = len(s[new:i]) + 1
        #     if maxc < l:
        #         maxc = l
        # return maxc


s = "aabaab!bb"
t = Solution()
print(t.lengthOfLongestSubstring(s))