'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
'''
class Solution:
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if len(strs) > 0:
			ss = set(strs)
			s = strs[0]
			letter = []
			minlen = len(min(strs,key = len))	#取strs中长度最小的str的长度
			for i in range(minlen):
				for strr in ss:
					if strr[i] == s[i]:
						continue
					else:
						return ''.join(letter)	#list转str拼成一个字符串用 ''.join( )
				letter.append(s[i])
			return ''.join(letter)
		else:
			return ''

t = Solution()
print(t.longestCommonPrefix(["flower","flow","flight"]))