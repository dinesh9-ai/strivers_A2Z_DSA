def rev(self,head):
        p=None
        c,n=head,head
        while n:
            n=c.next
            c.next=p
            p=c
            c=n
        return p    
    def addOne(self,head):
        #Returns new head of linked List
        if not head:
            return 1.
        q=self.rev(head)
        h=q
        a=1
        p=0
        while q:
            p=q
            f=(q.data+a)
            #print(f,a)
            a=(f)//10
            q.data=f%10
            q=q.next
        if a!=0:
            p.next=Node(a)
        return self.rev(h)
