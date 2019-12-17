# -*- encoding = utf-8 -*-
# Leetcode-19
# 使用双指针的方式，让其中一个指针先移动n步，然后再同时移动两个指针，注意边界情况。
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        q = head
        for i in range(n):
            p = p.next
        if not p:
            return head.next
        while p.next != None:
            p = p.next
            q = q.next
        q.next = q.next.next
        return head
