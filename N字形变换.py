'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 思路：构造对应行数的空列表，遍历，对一次折返取模
        #       超过列数之前向下插入，超过2n-2之前向上插入
        if numRows == 1:
            return s
        lst = []
        j = 0   #计行器
        once = 2*numRows - 2    #一次折返
        for a in range(numRows):#构造对应行数的空列表
            lst.append([])
        for i in range(len(s)): #遍历
            lst[j].append(s[i]) #插入计行器j对应列表
            if i%(once) < numRows - 1:  #判断是否超过行数，处理计行器j
                j += 1
            else:
                j -= 1
        get = [st for elem in lst for st in elem]#字符串铺平
        return ''.join(get)

s = "LEETCODEISHIRING"; numRows = 4
t = Solution()
print(t.convert(s, numRows))