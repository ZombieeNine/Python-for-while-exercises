P=float(input("Процент вклада: "))
if P>25 or P<0: 
    print("ERROR") 
    exit()
S1=1000
S2=1100
K=0
while S1<S2:
    S1*=1+P/100
    K+=1
    print(f"K = {K}, S = {S1} ")
print()
print(f"Кол-во месяцев = {K}, Итоговый размер вклада = {S1}")
