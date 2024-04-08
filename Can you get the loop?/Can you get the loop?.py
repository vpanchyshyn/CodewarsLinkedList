def loop_size(node):
    fast = node
    slow = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = node
            while fast!=slow:
                slow = slow.next
                fast = fast.next
            start = slow
            current = slow.next
            length = 1
            while start != current:
                current = current.next
                length += 1
            return length
