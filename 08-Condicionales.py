import os
os.system ("cls") 
p = 20
pc1 = float(input("Ingrese la nota del examen 1: "))
pc2 = float(input("Ingrese la nota del examen 2: "))
pc3 = float(input("Ingrese la nota del examen 3: "))
if pc1 <= 20 and pc2 <= 20 and pc3 <= 20:
   if pc1 >= 13 and pc2 >= 13 and pc3 >= 13: 
      propinatotal = p + 5 + 5 + 5
   else : 
      print("No recibirá propina")
      if pc1 >= 13 and pc2 < 13 and pc3 < 13: 
         propinaPC1 = p + 5
         print(f"Propina: {propinaPC1: .2f}")
      else : 
         print("NO RECIBE PROPINA ADICIONAL")
         if pc2 >= 13 and pc1 < 13 and pc3 < 13: 
            propinaPC2 = p + 5
            print(f"Propina: {propinaPC2: .2f}")
         else : 
            print("NO RECIBE PROPINA ADICIONAL")
            if pc1 < 13 and pc2 < 13 and pc3 >= 13: 
               propinaPC3 = p + 5
               print(f"Propina: {propinaPC3: .2f}")
            else : 
               print("NO RECIBE PROPINA")
else: 
   print("Ingrese notas validas de 0 a 20") 