import os
os.system ("cls")
angulo = int(input("Ingrese el ángulo en grados: "))
if angulo == 0: 
    print("Tipo de Ángulo: NULO")
if angulo > 0 and  angulo < 90: 
    print("Tipo de Ángulo: AGUDO")
if angulo == 90: 
    print("Tipo de Ángulo: RECTO")
if angulo > 90 and angulo < 180: 
    print("Tipo de Ángulo: OBTUSO")
if angulo >= 180 and angulo < 360: 
    print("Tipo de Ángulo: CÓNCAVO")
if angulo == 360: 
    print("Tipo de Ángulo: COMPLETO" )
elif angulo > 360: 
    print(" El ángulo que ingresó no pertenece a ninguna categoría")