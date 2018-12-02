'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符	I	V	X	L	C	D	M
数值	1	5	10	50	100	500	1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即
为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例
如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等
于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个
特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:			示例 2:			示例 3:
输入: "III"		输入: "IV"		输入: "IX"
输出: 3			输出: 4			输出: 9

示例 4:
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例 5:
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
'''
class Solution:
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		slen = len(s)
		ss = iter(range(slen))	#生成迭代器，以便于使用next()
		num = 0
		for i in ss:
			if s[i] == 'I':
				if i+1 < slen and s[i+1] == 'V':
					num = num + 4
					next(ss)
				elif i+1 < slen and s[i+1] == 'X':
					num = num + 9
					next(ss)
				else:
					num = num + 1
			elif s[i] == 'V':
				num = num + 5
			elif s[i] == 'X':
				if i+1 < slen and s[i+1] == 'L':
					num = num + 40
					next(ss)
				elif i+1 < slen and s[i+1] == 'C':
					num = num + 90
					next(ss)
				else:
					num = num + 10
			elif s[i] == 'L':
				num = num + 50
			elif s[i] == 'C':
				if i+1 < slen and s[i+1] == 'D':
					num = num + 400
					next(ss)
				elif i+1 < slen and s[i+1] == 'M':
					num = num + 900
					next(ss)
				else:
					num = num + 100
			elif s[i] == 'D':
				num = num + 500
			elif s[i] == 'M':
				num = num + 1000
			else:
				break
		return num

t = Solution()
print(t.romanToInt('MCMXCIV'))