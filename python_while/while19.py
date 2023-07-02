N=int(input("N: "))
c=0
while N>=1:
    x=N%10
    N=int(N/10)
    c=c*10+x
print("Новое число:",c)
