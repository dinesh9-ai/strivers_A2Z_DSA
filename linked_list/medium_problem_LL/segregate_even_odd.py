def segregate(head):
    eh,oh=None,None
    e,o=None,None
    h=head
    while h:
        if h.data%2==0:
            if not e:
                e=h
                eh=h
            else:
                e.next=h
                e=e.next
        else:
            if not o:
                o=h
                oh=h
            else:
                o.next=h
                o=o.next
        h=h.next
    if not eh:
        return oh
    if not oh:
        return eh
    e.next=oh
    o.next=None
    return eh
