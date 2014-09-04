__author__ = 'Administrator'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge_list(head1, head2):
    fakehead = ListNode(0)
    lastnode = fakehead
    while head1 != None and head2 != None:
        if head1.val <= head2.val:
            lastnode.next = head1
            lastnode = head1
            head1 = head1.next
        else:
            lastnode.next = head2
            lastnode = head2
            head2 = head2.next
    if head1:
        lastnode.next = head1
    if head2:
        lastnode.next = head2
    return fakehead.next

def print_list(head):
    while head != None:
        print head.val
        head = head.next

array1 = [13]
array2 = [1, 12, 22, 25]
fakehead1 = ListNode(0)
lasthead1 = fakehead1
for a in array1:
    lasthead1.next = ListNode(a)
    lasthead1 = lasthead1.next
fakehead2 = ListNode(0)
lasthead2 = fakehead2
for a in array2:
    lasthead2.next = ListNode(a)
    lasthead2 = lasthead2.next

print_list(fakehead1.next)
print_list(fakehead2.next)
print '======================='
print_list(merge_list(fakehead1.next, fakehead2.next))