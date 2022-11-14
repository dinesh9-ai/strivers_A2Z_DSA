def ror(head,k):
    if not head or not head.next or l==0:
        return head
    l=1
    t=head
    while t.next:
        t=t.next
        l+=1
    t.next=head
    k=k%l
    t=head
    e=l-k
    while e:
        t=t.next
        e-=1
    head=t.next
    t.next=None
    return head
    
    
