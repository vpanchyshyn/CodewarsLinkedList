def stringify(node):
    res = []
    probe = node
    while probe is not None:
        res.append(str(probe.data))
        probe = probe.next
    res.append('None')
    return ' -> '.join(res)
