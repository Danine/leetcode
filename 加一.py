'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例 1:                         示例 2:
输入: [1,2,3]                   输入: [4,3,2,1]
输出: [1,2,4]                   输出: [4,3,2,2]
解释: 输入数组表示数字 123       解释: 输入数组表示数字 4321。
'''
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(i) for i in digits]   #按位转str
        digits = ''.join(digits)            #字符串拼接
        digits = int(digits)                #转为int然后加一
        digits += 1
        digits = str(digits)                #转回字符串
        digits = list(digits)               #转列表
        digits = [int(i) for i in digits]   #按位转回int
        # 一行版
        digits = [int(i) for i in list(str(int(''.join([str(i) for i in digits])) + 1))]
        return digits

digits = [9,9,9,9]
t = Solution()
print(t.plusOne(digits))