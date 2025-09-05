# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        curr = head 
        decimal_num = 0
        while curr:
            decimal_num = decimal_num * 2 + curr.val
            curr = curr.next
        return decimal_num

        