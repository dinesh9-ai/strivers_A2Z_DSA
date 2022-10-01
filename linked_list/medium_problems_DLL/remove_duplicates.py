class node:
    def __init__(self,val,nxt=None,prev=None):
        self.val=val
        self.nxt=nxt
        self.prev=prev
class doubly:
    def __init__(self,head=None):
        self.head=head

    def insertEnd(self,val):
        if not self.head:
            self.head=node(val)
            return
        h=self.head
        while h.nxt:
            h=h.nxt
        temp=node(val)
        temp.prev=h
        h.nxt=temp
        return

    def delAll(self,x):
        if not self.head: return
        p,h=None,self.head
        while h:
            if h.val==x:
                print(h.val)
                if not p:
                    self.head=h.nxt
                else:
                    p.nxt=h.nxt
            p=h
            h=h.nxt
    def Print(self):
        h=self.head
        while h:
            print(h.val,end='<->')
            h=h.nxt
        print('NULL')

a=[1,2,3,4,5,3,6,7,9,3]
ll=doubly()
for i in a:
    ll.insertEnd(i)
ll.Print()
ll.delAll(3)
ll.Print()
