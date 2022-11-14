def merge(a,b):
    t=node(0)
    r=t
    while a and b:
        if a.data<b.data:
            t.bottom=a
            a=a.bottom
            t=t.bottom
        else:
            t.bottom=b
            b=b.bottom
            t=t.bottom
    if a:
        t.bottom=a
    else:
        t.bottom=b
    return r.bottom
def flat(a):
    if not a or not a.next:
        return a
    a.next=flat(a)
    a=merge(a,a.next)
    return a
