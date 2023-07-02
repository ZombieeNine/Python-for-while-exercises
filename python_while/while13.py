A=float(input("A: "))
K = 1
S = 1
while S <= A:
    K += 1
    x = 1/K
    S += 1/K
    print("K = {0}, 1/K = {1} S = {2}".format(K,x,S))
print()
print("K = {0}, S = {1}".format(K,S))