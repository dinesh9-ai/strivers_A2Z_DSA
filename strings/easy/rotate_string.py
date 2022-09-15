a="bbbacddceeb"
b="ceebbbbacdd"

def isp(s,goal):
    return goal in s+s
print(isp(a,b))
