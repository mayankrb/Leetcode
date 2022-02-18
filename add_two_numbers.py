# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        added_list_head = None
        added_list_rear = None
        carry = 0
        #till both lists have elements
        while l1 and l2:
            cur_sum = l1.val + l2.val + carry
            if cur_sum >= 10:
                carry = 1
                cur_sum -= 10
            else:
                carry = 0
            
            if not added_list_head:
                #if no element yet
                added_list_head = ListNode(cur_sum)
                added_list_rear = added_list_head
            else:
                added_list_rear.next = ListNode(cur_sum)
                added_list_rear = added_list_rear.next
            l1 = l1.next
            l2 = l2.next
        
        #if there are  some elements remaining in the first list
        while l1:
            cur_sum = l1.val + carry
            if cur_sum >= 10:
                carry = 1
                cur_sum -= 10
            else:
                carry = 0
            added_list_rear.next = ListNode(cur_sum)
            added_list_rear = added_list_rear.next
            l1 = l1.next
        
        #if there are  some elements remaining in the second list
        while l2:
            cur_sum = l2.val + carry
            if cur_sum >= 10:
                carry = 1
                cur_sum -= 10
            else:
                carry = 0
            added_list_rear.next = ListNode(cur_sum)
            added_list_rear = added_list_rear.next
            l2 = l2.next
        #if carry 1 is remaining then add the last node
        if carry == 1:
            added_list_rear.next = ListNode(1)
            added_list_rear = added_list_rear.next
        return added_list_head