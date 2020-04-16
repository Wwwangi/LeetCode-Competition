# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pointer1=l1
        pointer2=l2
        while pointer1 and pointer2:
            pointer2.val=pointer1.val+pointer2.val
            temp=pointer2
            pointer1=pointer1.next
            pointer2=pointer2.next       
        if pointer1:
            temp.next=pointer1
        temp=l2
        while l2:
            if(l2.val>=10):
                if l2.next:
                    l2.next.val+=l2.val//10
                    l2.val%=10
                else:
                    l2.next=ListNode(l2.val//10)
                    l2.val%=10
            l2=l2.next
        return temp
            