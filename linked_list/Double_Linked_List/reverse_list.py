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

    def reverseL(self):
        """
        Reverse the given List
        """
        if not self.head:
            return
        h=self.head
        q=0
        while h:
            h.nxt,h.prev=h.prev,h.nxt
            q=h
            h=h.prev
        self.head=q
        
                
            
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
ll.reverseL()
ll.Print()

