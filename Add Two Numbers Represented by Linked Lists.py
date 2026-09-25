
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        
        if l1: 
          l1 = l1.next
        if l2: 
          l2 = l2.next
    return dummy_head.next

def build_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for val in elements[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


n1=int(input())
n1_lst=list(map(int,input().split()))

n2=int(input())
n2_lst=list(map(int,input().split()))

l1 = build_list(n1_lst)
l2 = build_list(n2_lst)

result_head = addTwoNumbers(l1, l2)

import copy
temp=copy.copy(result_head)
while temp:
  print(temp.val,end=" ")
  temp=temp.next
