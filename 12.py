import os
os.system("cls")
ss = int(input("Número expresado en segundos: "))
dias = ss// (24 * 60 * 60)
ss = ss % (24 * 60 * 60)
hors = ss // (60 * 60)
ss = ss % (60 * 60)
mints = ss // 60
ss = ss % 60
print ("En días: {}".format(dias))
print ("En horas: {}".format(hors))
print ("En minutos: {}".format(mints))
print ("En segundos: {}".format(ss))