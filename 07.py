import os
os.system ("cls")
lg = float(input("Largo del rectángulo: "))
an = float(input("Ancho del rectángulo: "))
area = lg * an
perimetro = 2 * (lg + an )
print(f"Área: {area: .2f} m" )
print(f"Perímetro: {perimetro: .2f} m")