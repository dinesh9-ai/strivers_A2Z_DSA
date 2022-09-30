def nthNode(self,n):
    d=node()
    d.next=h
    f,s=d,d
    for i in range(1,n+1):
        f=f.next
    while f.next:
        f=f.next
        s=s.next
    s.next=s.next.next
    
