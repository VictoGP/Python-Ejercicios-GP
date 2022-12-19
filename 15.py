import os
os.system("cls")

j = float(input("Aporte de Juan: "))
r = float(input("Aporte de Rosa: "))
dS = float(input("Aporte de Daniel: "))
dD = dS / 3.00
Total = j + r + dD
PJuan = (j * 100) / Total
PRosa = (r * 100) / Total
PDaniel = (dD * 100) / Total
print(f"conversión de soles a dolares de Daniel {dD:.2f}")
print ( f"Total: {Total:.2f} ")
print( f"Porcentaje de Juan :  {PJuan:.2f}")
print( f"Porcentaje de Rosa :  {PRosa:.2f}")
print( f"Porcentaje  de Daniel :  {PDaniel:.2f}")