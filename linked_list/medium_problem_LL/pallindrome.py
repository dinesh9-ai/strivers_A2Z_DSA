def isp(r):
    if not r:
        return 1
    r1=isp(r)
    r1=r1 and (r.val==self.l.val)
    self.l=self.l.next
    return r1
