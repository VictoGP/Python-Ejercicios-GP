import os
os.system ("Cls")

d = float(input("Ingrese el monto de la donación: "))
centroSalud = ((25*d)/100)
ComedorInfantil = ((35*d))/100
escuelaInfantil = ((25*d))/100 
asiloAncianos = ((15*d))/100
print(f" Porcentaje para el Centro de Salud: {centroSalud: .2f}")
print(f" Porcentaje para el  Comedor Infantil: {ComedorInfantil: .2f}")
print(f" Porcentaje para la Escuela Infantil: {escuelaInfantil: .2f}")
print(f" Porcentaje para el Asilo de Ancianos: {asiloAncianos: .2f}")