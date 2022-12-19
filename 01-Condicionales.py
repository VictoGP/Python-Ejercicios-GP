import os
os.system("cls")

n = float(input("Cantidad de productos: "))

if n <= 25:
    importe = n * 27
    descuento = importe * 0.05
    ipagar = importe - descuento
    print(importe)
    print (f"Importe total a pagar: {ipagar: 2f}")
elif n > 25 and n < 50:
    importe = n * 25
    descuento = importe * 0.05
    ipagar = importe - descuento
    print(importe) 
    print (f"Importe total a pagar: {ipagar: 2f}")
else :
    importe = n * 23
    print ("Aplica Descuento del 15%")
    descuento = importe * 0.15
    ipagar = importe - descuento
    print(importe)
    print (f"Importe total a pagar: {ipagar: 2f}")