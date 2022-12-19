import os
os.system ("cls") 
print(" 1.  Cóigo 101")
print(" 2.  Cóigo 102")
print(" 3.  Cóigo 103")
print(" 4.  Cóigo 104")
c = float(input("Número de código: "))
if c == 1 :
    nUnidades = float(input("Ingrese la cantidad de unidades que desea comprar: "))
    importedCompra = 17 * nUnidades
    if nUnidades >= 1 and nUnidades<= 10:
       descuento = (5*importedCompra)/100
       importePagar = importedCompra - descuento
       print(f"Importe de compra: {importedCompra: .2f}")
       print(f"Descuento: {descuento: .2f}")
       print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 11 and nUnidades <= 20:
        descuento = (8*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 21 and nUnidades <= 30:
        descuento = (10*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 31:
        descuento = (13*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")

if c == 2:
    nUnidades = float(input("Ingrese la cantidad de unidades a comprar: "))
    importedCompra = 25 * nUnidades
    if nUnidades >= 1 and nUnidades<= 10:
       descuento = (5*importedCompra)/100
       importePagar = importedCompra - descuento
       print(f"Importe de compra: {importedCompra: .2f}")
       print(f"Descuento: {descuento: .2f}")
       print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 11 and nUnidades <= 20:
        descuento = (8*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 21 and nUnidades <= 30:
        descuento = (10*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 31:
        descuento = (13*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")

if c == 3 :
    nUnidades = float(input("Ingrese la cantidad de unidades a comprar: "))
    importedCompra = 16 * nUnidades
    if nUnidades >= 1 and nUnidades<= 10:
       descuento = (5*importedCompra)/100
       importePagar = importedCompra - descuento
       print(f"Importe de compra: {importedCompra: .2f}")
       print(f"Descuento: {descuento: .2f}")
       print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 11 and nUnidades <= 20:
        descuento = (8*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 21 and nUnidades <= 30:
        descuento = (10*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 31:
        descuento = (13*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")

if c == 4 :
    nUnidades = float(input("Ingrese la cantidad de unidades a comprar: "))
    importedCompra = 27 * nUnidades
    if nUnidades >= 1 and nUnidades<= 10:
       descuento = (5*importedCompra)/100
       importePagar = importedCompra - descuento
       print(f"Importe de compra: {importedCompra: .2f}")
       print(f"Descuento: {descuento: .2f}")
       print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 11 and nUnidades <= 20:
        descuento = (8*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 21 and nUnidades <= 30:
        descuento = (10*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")
    elif nUnidades >= 31:
        descuento = (13*importedCompra)/100
        importePagar = importedCompra - descuento
        print(f"Importe de compra: {importedCompra: .2f}")
        print(f"Descuento: {descuento: .2f}")
        print(f"Importe a Pagar: {importePagar: .2f}")

elif c != 1 and c != 2 and c != 3 and c != 4:
    print(" ERROR - el valor ingresado No es un código")
    

