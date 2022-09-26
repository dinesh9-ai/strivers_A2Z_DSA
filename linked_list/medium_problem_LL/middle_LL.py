class node:
    def __init__(self,val,nxt=None):
        self.val=val
        self.nxt=nxt

class LL:
    def __init__(self,head=None):
        self.head=head

        
    def insert_node(self,x):
        if not self.head:
            self.head=node(x)
            return
        h=self.head
        while h.nxt:
            h=h.nxt
        h.nxt=node(x)

        
    def findMiddle(self):
        """
        To find the middle element
        """
        if not self.head:
            return "Not Found"
        s,f=self.head,self.head
        while f and f.nxt:
            s=s.nxt
            f=f.nxt.nxt
        return s.val
    

a=[10,20,40,80,6]
ll=LL()
for i in a:
    ll.insert_node(i)
print(ll.findMiddle())

