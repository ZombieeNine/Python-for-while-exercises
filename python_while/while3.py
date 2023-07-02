n = int(input("N: "))
k = int(input("K: "))
r = n
q = 0
while r >= k:
    r -= k
    q += 1
print("Частное: ", q)
print("Остаток: ", r)