
n = int(input("número de 4 cifras: "))
d4 = n % 10
d3 = int((n % 100) / 10)
d2 = int((n % 1000) / 100)
d1 = int((n - (n % 1000)) / 100)
print (f"Digito 1: {d1: .2f}")
print (f"Digito 2: {d2: .2f}")
print (f"Digito 3: {d3: .2f}")
print (f"Digito 4: {d4: .2f}")
if d1 > d2 and d1 > d3  and d1 > d4: 
    print(f"Dígito mayor: {d1: .2f}")
    dM = (d1 / 10) 
    print(f"Número mayor: {dM: .2f}9")
if d2> d1 and d2 > d3  and d2 > d4: 
    print(f"Dígito mayor: {d2: .2f}")
    print(f"Número mayor: {d2: .2f}9")
if d3 > d1 and d3 > d2  and d3 > d4: 
    print(f"Dígito mayor: {d3: .2f}")
    print(f"Número mayor: {d3: .2f}9")
if d4 > d1 and d4 > d2  and d4 > d3: 
    print(f"Dígito mayor: {d4: .2f}")
    print(f"Número mayor: {d4: .2f}9")
else :
    print("VALOR INCORRECTO")