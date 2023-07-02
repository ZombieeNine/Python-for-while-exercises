N=int(input("N: "))
i=0
c=False
while N>=1:
    i+=1
    x=N%10
    if x==2:
        c=True
        break
    N=int(N/10)
print(c)

