import datetime
hora = datetime.datetime.now()
print("HORA ACTUAL: ", hora)
hora_aproximada = hora + datetime.timedelta(minutes=45)
print ("Dentro de 45 minutos la hora será: " )
print (hora_aproximada)