n1 = int(input("nota1 : "))
n2 = int(input("nota2: "))
n3 = int(input("nota3: "))
if n3 > 10 and n3 <=18 and n1 < 21 and n2 < 21: 
   n3conPuntos = n3 + 2
   print(f"Nota de la PC3 con puntos agregados: {n3conPuntos: .2f}")
   p = (n1 + n2 + n3conPuntos) / 3
   print(f"PROMEDIO: {p: .2f}")
elif n1 > 20 or n2 > 20 or n3 > 20: 
   print(f"NOTA INCORRECTA")
else: 
   p = (n1 + n2 + n3) / 3
   print(f"PROMEDIO: {p: .2f}")