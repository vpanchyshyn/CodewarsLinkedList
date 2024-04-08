class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise Exception
    odd_head = None
    even_head = None
    odd_current = None
    even_current = None
    current = head
    counter = 1
    while current:
        if counter % 2:
            if not odd_head:
                odd_head = current
                odd_current = current
            else:
                odd_current.next = current
                odd_current = odd_current.next
        else:
            if not even_head:
                even_head = current
                even_current = current
            else:
                even_current.next = current
                even_current = even_current.next
        current = current.next
        counter += 1
    if odd_current:
        odd_current.next = None
    if even_current:
        even_current.next = None
    return Context(odd_head, even_head)
    
