import os
os.system("cls")
radio = float(input("Radio del ilindro: "))
altura = float(input("Altura del cilindro: "))
pi = 3.141592
areabase = pi * (radio ** 2)
arealateral = 2 * pi * radio * altura
areatotal = 2 * areabase * arealateral
print(f"Área Base: {areabase: .2f} m")
print(f"Área lateral : {arealateral: .2f} m")
print(f"ÁREA TOTAL: {areatotal: .2f} m")