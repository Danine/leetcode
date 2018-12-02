'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:			示例 2:			示例 3:
输入: 123			输入: -123		输入: 120
输出: 321			输出: -321		输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''
class Solution:
    def reverse(self, x):
        if x < 0:
            s = str(-x)
            y = s[::-1]	#将str倒序输出
            z = -int(y)
        else:
            s = str(x)
            y = s[::-1]
            z = int(y)
        if -2**31<z<2**31-1:
            return z
        return 0
