s='aaaaaaaaaaaaaaaaaab'
p='aaab'

def lps(p,a):
    a[0]
    l=0
    i=1
    m=len(p)
    while i<m:
        if p[i]==p[l]:
            l=l+1
            a[i]=l
            i+=1
        elif p[i]!=p[l]:
            if l!=0:
                l=a[l-1]
            else:
                a[i]=0
                i+=1
def searchh(s,p):
    a=[0]*len(p)
    lps(p,a)
    i,j=0,0
    n,m=len(s),len(p)
    while i<n:
        if p[j]==s[i]:
            i+=1
            j+=1
            if j==m:
                print(i-j)
                j=a[j-1]
        elif i<n and p[j]!=s[i]:
            if j>0:
                j=a[j-1]
            else:
                i+=1
        
searchh(s,p)
