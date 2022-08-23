def pal(s,i,j):
    if i>=j:
        return True
    if s[i]!=s[j]:
        return False
    return pal(s,i+1,j-1)

print(pal('abbd',0,3))
