A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
a=0
b=0
while A>=C:
    A-=C
    a+=1
while B>=C:
    B-=C
    b+=1
k=0
i=0
while i<a:
    i+=1
    x=0
    while x<b:
        x+=1
        k+=1
print("Количество квадратов на прямоугольнике:",k)