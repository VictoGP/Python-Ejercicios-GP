import os
os.system("cls")
r = float(input("Ingrese el radio del cilindro: "))
al = float(input("Ingrese la altura del cilindro: "))
pi = 3.141592
area = 2 * pi * r * (r + al) 
v = pi * ( r ** 2 ) * al
print(f"Área Total: {area: .2f} m²")
print(f"Volumen: {v : .2f} m³")