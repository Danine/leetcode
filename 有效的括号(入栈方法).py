'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，
判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:			示例 2:			示例 3:	
输入: "()"		输入: "()[]{}"	输入: "(]"
输出: true		输出: true		输出: false

示例 4:			示例 5:
输入: "([)]"	输入: "{[]}"
输出: false		输出: true
'''
class Solution:
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		if s =='':
			return True
		elif s[0] == ')' or s[0] == '}' or s[0] == ']':
			return False
		slen = len(s)
		ss = iter(range(slen))
		stack = []
		try:
			for i in ss:
				if s[i] == '(' or s[i] == '{' or s[i] == '[':
					stack.append(s[i])
				elif (s[i] == ')' and stack[-1] == '(') or \
					(s[i] == '}' and stack[-1] == '{') or \
					(s[i] == ']' and stack[-1] == '['):			#stack[-1]表示栈顶
					stack.pop()
				else:
					return False
		except :
			return False

		if len(stack) == 0:
			return True
		else:
			return False

t = Solution()
print(t.isValid("(])"))