def intersect(headA,headB):
    h1,h2=headA,headB
    c1,c2=0,0
    while h1:
        c1+=1
        h1=h1.next
    while h2:
        c2+=1
        h2=h2.next
    h1=headA
    h2=headB
    #print(c1,c2)
    if c1>c2:
        while c1>c2 and h1:
            h1=h1.next
            c1-=1
    else:
        while c1<c2 and h2:
            h2=h2.next
            c2-=1
    #print(c1,c2)
    while h1 and h2:
        if h1==h2:
            return h1
        h1=h1.next
        h2=h2.next
    return None
