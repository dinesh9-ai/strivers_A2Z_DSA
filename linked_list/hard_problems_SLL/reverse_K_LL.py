def reverseK(slef,k):
    if not self.head or k==1:
        return
    h=self.head
    d=Node(0)
    d.next=h
    c,n,p=d,d,d
    cu=0
    while c.next:
        c=c.next
        cu+=1
    while cu>=k:
        c=p.next
        n=c.next
        for i in range(1,k):
            c.next=n.next
            n.next=p.next
            p.next=n
            n=c.next
        p=c
        cu-=k
    return d.next
