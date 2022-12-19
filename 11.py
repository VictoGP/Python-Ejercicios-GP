import os
os.system("cls")
n1 = int(input ("Número entero de 3 cifras: "))
n2 = int(input ("Número entero de 3 cifras: "))
c3 = n1 % 10
c2 = int((n1 % 100) / 10)
c1 = int((n1 % 1000) / 100)
d3 = n2 % 10
d2 = int((n2 % 100) / 10)
d1 = int((n2 % 1000) / 100)
print(f"{d3}{c2}{d1}")
print(f"{c3}{d2}{c1}")