#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : guanglinzhou(z00522822)
# @Version : $Id$

"""
思路：
1、顺序迭代两个链表，得出正数值，相加后将和构造新的链表并返回
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def _addTwoNumbers_brute_force(self, l1, l2):
        val1, val2 = '', ''
        while l1.next:
            val1 += str(l1.val)
            l1 = l1.next
        val1 += str(l1.val)
        val1 = int(val1[::-1])

        while l2.next:
            val2 += str(l2.val)
            l2 = l2.next
        val2 += str(l2.val)
        val2 = int(val2[::-1])

        res = val1 + val2
        res_list = list(str(res))[::-1]
        res_head = ListNode(int(res_list[0]))
        ptr = res_head
        for i, item in enumerate(res_list):
            if not i:
                continue
            ptr.next = ListNode(int(item))
            ptr = ptr.next
        return res_head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self._addTwoNumbers_brute_force(l1, l2)

    def test(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        print(self.addTwoNumbers(l1, l2))


solution = Solution()
solution.test()
