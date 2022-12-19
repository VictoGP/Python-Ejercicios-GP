import os
os.system("cls")

ft = float(input("Estatura en pies: "))
i = float(input("Estatura en pulgadas: "))
print( f"Estatura inglesa:  {ft:} ft - {i:} in")
ftam = ft * (1.0 / 3.28084)
inenm = i * (1.0 / 39.3701)
e = ftam + inenm  
print( f"La estatura en metros sería: {e: .2f} m") 