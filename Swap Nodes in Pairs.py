__author__ = 'samsung'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def swapPairs( head):
    if head is None:
        return head
    elif head.next is None:
        return head
    p0 = ListNode(0)
    p0.next = head
    p1 = head
    p2 = head.next
    p3 = head.next.next
    head = p2
    while p3:
        p0.next = p2
        p2.next = p1
        p1.next = p3
        p0 = p1
        p1 = p3
        p2 = p1.next
        if p2:
            p3 = p2.next
        else:
            break
    if p3 is None:
        p0.next = p2
        p2.next = p1
        p1.next = p3
    return head

def disp(head):
    index = head
    while index != None:
        print index.val
        index = index.next

head = ListNode(1)
a = ListNode(2)
head.next = a
b = ListNode(3)
a.next = b
c = ListNode(4)
b.next = c
disp(swapPairs(head))

