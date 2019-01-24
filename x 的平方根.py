'''
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
示例:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,由于返回类型是整数，小数部分将被舍去。
'''
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # return int(x**0.5)#最快
        #int最大到2147483647，开方46340，用二分法
        high = 46340
        low = 0
        while low <= high:
            mid = int((low + high) / 2)
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                low = mid + 1
            elif mid**2 > x:
                high = mid - 1
        return high
        
test = [0,1,2,3,8,10,15]
t = Solution()
for i in test:
    print(t.mySqrt(i))