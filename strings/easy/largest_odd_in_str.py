num="35427"
res = ""
for i in range(len(num)-1,-1,-1):
    if int(num[i])&1:
        return num[:i+1]
return res
