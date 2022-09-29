def detect_loop(self):
    h=self.head
    while h and h.val>1000:
        h.val=abs(h.val)+1001
        h=h.nxt
    return h
