N=int(input("N: "))
K = 0
P = 1
while P < N:
    P *= 3
    K += 1
K -= 1
print("K={0},3^K={1},3^(K+1)={2}".format(K,3**K,3**(K+1)))