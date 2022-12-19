import os
os.system("cls")
gig =float(input("Capacidad del disco duro en GB: "))

byte = gig * 1024 * 1024 * 1024
megabyte = gig * 1024
kilobyte = gig * 1024 * 1024 
print(f"Capacidad del disco duro: {gig: .2f} GB")
print( f"MEGABYTES: {megabyte: .2f} MG")
print( f"KILOBYTES: {kilobyte: .2f} KG")
print( f"BYTES: {byte: .2f} B")