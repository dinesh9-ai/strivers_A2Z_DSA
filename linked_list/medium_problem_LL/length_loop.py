def loopLength(self):
    h=self.head
    while h and h.data<10**5:
        h.data=h.data+(1+10**5)
        h=h.next
    if not h: return 0
    h.data=h.data-(1+10**5)
    c=1
    h=h.next
    while h.data>10**5:

        c+=1
        h=h.next
    return c
