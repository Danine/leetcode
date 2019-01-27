'''
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
示例 1:                  示例 2:
输入:   1         1      输入:   1          1
       / \       / \            /           \
      2   3     2   3          2             2
     [1,2,3],  [1,2,3]       [1,2],     [1,null,2]
输出: true               输出: false
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False

p = [1,2,3]
q = [1,2,3]
t = Solution()
print(t.isSameTree(p,q))