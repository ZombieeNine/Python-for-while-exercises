N=int(input("N: "))
while N>=1:
    x = N%10
    print(x,end="; ")
    N = int(N/10)