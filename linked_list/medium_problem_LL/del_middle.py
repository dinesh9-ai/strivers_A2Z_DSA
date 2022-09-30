def delMiddle(self):
    s,f=self.head,self.head
    while f and f.next:
        f=f.next.next
        p=s
        s=s.next
    p.next=s.next
    
