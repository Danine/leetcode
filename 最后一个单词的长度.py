'''
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指由字母组成，但不包含任何空格的字符串。
示例:
输入: "Hello World"
输出: 5
'''
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()#去除字符串两端空格
        count = 0
        leng = len(s)
        for i in range(leng-1,-1,-1):#倒序遍历
            if s[i] != ' ':
                count += 1
            else:
                return count
        return count
s = "a "
t = Solution()
print(t.lengthOfLastWord(s))