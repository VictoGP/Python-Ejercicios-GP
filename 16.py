
import os 
os.system ("cls")
nhoras = float(input("cantidad de horas trabajadas: "))
sB = nhoras * 10
sBruto = ((20*sB)/100) + sB
sNeto = sBruto - ((10*sBruto)/100) 
print(f"Sueldo Básico: {sB: .2f} ")
print(f"Sueldo Bruto: {sBruto: .2f} ")
print(f"Sueldo Neto: {sNeto: .2f}")