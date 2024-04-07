def swap_pairs(head):
    temp = Node()
    temp.next = head
    prev = temp
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return temp.next
