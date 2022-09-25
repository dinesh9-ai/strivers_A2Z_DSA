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

    def deletenode(self,x):
        """
        Deleting a Node
        """
        if not self.head:
            return
        if self.head.val==x:
            temp=self.head.nxt
            del self.head
            self.head=temp
            return
        h=self.head
        while h.nxt:
            if h.nxt.val==x:
                if h.nxt.nxt:
                    h.nxt.nxt.prev=h
                    h.nxt=h.nxt.nxt
                else:
                    del h.nxt
                    h.nxt=None
                return
            h=h.nxt
                
            
    def Print(self,rev=False):
        h=self.head
        if h==None:
            print('NULL')
            return
        if not rev:
            while h:
                print(h.val,end='<->')
                h=h.nxt
            print('NULL')
        else:
            while h.nxt:
                h=h.nxt
            while h.prev:
                print(h.val,end='<->')
                h=h.prev
            print('NULL')

a=[1,2,3,4]
ll=doubly()
for i in a:
    ll.insertEnd(i)
ll.deletenode(1)
ll.Print(rev=1)

