def clone(head):
    h=head
    while h:
        t=node(h.val)
        t.next=h.next
        h.next=t
        h=h.next.next
    h=head
    while h:
        if h.random:
            h.next.random=h.random.next
        h=h.next.next
    d=node(0)
    h=head
    t=d
    f=d
    while h:
        f=h.next.next
        t.next=h.next
        h.next=f
        t=t.next
        h=f
    return d.next
        
