def sorts(head):
    h=head
    t=Node()
    q,w,r=None,None,None
    h1,h2,h3=t,t,t
    while h:
        if h.val==0:
            if not h1:
                q=h
            h1.next=h
            h1=h1.next
        elif h.val==1:
            if not h2:
                w=h2
            h2.next=h
            h2=h2.next
        else:
            if not h3:
                r=h3
            h3.next=h
            h3=h3.next
        h=h.next

        h1.next= w if w else r
        h2.next=h3

        if not q and not w:
            return r
        if not q:
            return r
        return q

    
        
