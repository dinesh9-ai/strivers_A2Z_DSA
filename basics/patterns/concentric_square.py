n=int(input())
for i in range(1,2*n):
    k=n
    if i<=n:
        for j in range(1,2*n):
            print(k,end='')
            if i>j:
                k=k-1
            if i+j>=2*n:
                k+=1
    if(i>n):
        for j in range(1,2*n):
            print(k,end='')
            if i+j<2*n:
                k=k-1
            if j>=i:
                k+=1
    print()
            
"""

5
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555


"""
