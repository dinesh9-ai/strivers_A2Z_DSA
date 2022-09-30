def addTwoNumbers(l1,l2):
        d=ListNode()
        t=d
        c=0
        s=0
        while l1 or l2 or c:
            s=0
            if l1:
                s+=l1.val
                l1=l1.next
            if l2:
                s+=l2.val
                l2=l2.next
            s+=c
            c=s//10
            t.next=ListNode(s%10)
            t=t.next
        return d.next
