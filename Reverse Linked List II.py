def reverseBetween(head, m, n):
    if head.next == None or m == n:
        return head
    index1 = ListNode(0)
    index2 = head
    index1.next = index2
    i = 1
    while i < m:
        index1 = index2
        index2 = index2.next
        i += 1
    before_node = index1
    index1 = index2
    index2 = index2.next
    reverse_list = []
    while i < n:
        reverse_list.append(index1)
        index1 = index2
        index2 = index2.next
        i += 1
    reverse_list.append(index1)
    after_node = index2
    if m == 1:
        head = reverse_list[-1]
    else:
        before_node.next = reverse_list[-1]
    for i in range(len(reverse_list) - 1):
        reverse_list[-i - 1].next = reverse_list[-i - 2]
    reverse_list[0].next = after_node
    return head


def disp(head):
    index = head
    while index != None:
        print index.val
        index = index.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
index = a

a = reverseBetween(a, 3, 3)
print '***5***'
disp(a)
