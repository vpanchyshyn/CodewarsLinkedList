def linked_list_from_string(s):
    if s == 'None':
        return None
    nodes = s.split(" -> ")
    head = Node(int(nodes[0]))
    current = head
    for node in nodes[1:]:
        if node == "None":
            break
        current.next = Node(int(node))
        current = current.next
    return head
