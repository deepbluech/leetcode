__author__ = 'samsung'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def find_middle(head):
    if head is None:
        return head
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
    return slow


def reverse(head):
    prehead = ListNode(0)
    while head != None:
        act_next = head.next
        second = prehead.next
        prehead.next = head
        head.next = second
        head = act_next
    return prehead.next


def merge(head1, head2):
    prehead = ListNode(0)
    last = prehead
    while head1 != None or head2 != None:
        if head1 == None:
            last.next = head2
            return prehead.next
        if head2 == None:
            last.next = head1
            return prehead.next
        saved_head1_next = head1.next
        saved_head2_next = head2.next
        last.next = head1
        head1.next = head2
        last = head2
        head1 = saved_head1_next
        head2 = saved_head2_next
    return prehead.next

def disp(head):
    while head != None:
        print head.val
        head = head.next


if __name__ == '__main__':
    head = ListNode(1)
    last = head
    for i in range(2, 8):
        cur = ListNode(i)
        last.next = cur
        last = cur
    last.next = None
    disp(head)
    mid = find_middle(head)
    print 'middle: %d' % find_middle(head).val
    print '====reverse second part===='
    reverse_head = reverse(mid.next)
    disp(reverse_head)
    print '====merge===='
    mid.next = None
    disp(merge(head, reverse_head))