'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''
class Solution:
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		l = []
		while l1 != [] and l2 != []:
			if l1[0] > l2[0]:
				l.append(l2[0])
				del l2[0]
			else:
				l.append(l1[0])
				del l1[0]
		if l1 == []:
			l += l2
		elif l2 == []:
			l += l1
		print(l)

t = Solution()
l1 = [1,2,4]; l2 = [2,3,4,7]
t.mergeTwoLists(l1,l2)