import os
os.system("cls")
n = int(input ("Número natural de 4 cifras: "))
c4 = n % 10
c3 = int((n % 100) / 10)
c2 = int((n % 1000) / 100)
c1 = int((n - (n % 1000)) / 1000)
sumatoria = c4 + c3 + c2 + c1
print(sumatoria)
print(f"La Sumatoria de {n: .2f} es: {sumatoria: .2f}")