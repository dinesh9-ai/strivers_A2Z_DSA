def facto(s,f):
    if f==1:
        return s
    return facto(s*f,f-1)
print(facto(1,5))
