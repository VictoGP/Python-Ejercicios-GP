import os
os.system("cls")
n = int(input ("Número natural de 4 cifras: "))
c4 = n % 10
c3 = int((n % 100) / 10)
c2 = int((n % 1000) / 100)
c1 = int((n - (n % 1000)) / 1000)
print(c4)
print(c3)
print(c2)
print(c1)
print(f"{c4}{c3}{c2}{c1}") 