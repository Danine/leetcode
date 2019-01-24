'''
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。
示例 1:                     示例 2:
输入: a = "11", b = "1"     输入: a = "1010", b = "1011"
输出: "100"                 输出: "10101"
'''
#bin()、oct()、int()、hex()为2、8、10、16进制
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2)
        b = int(b,2)
        return bin(a + b)[2:]#[2:]从下标2到结尾
        # return bin(int(a,2) + int(b,2))[2:]#一行版

t = Solution()
print(t.addBinary('1010','1011'))#默认为十进制，所以必须以字符串输入