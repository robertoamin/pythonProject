

monto=float(input("ingrese el monto a prestar: "))
interes=float(input("ingrese la tasa de interes: "))
numeroanios=int(input("ingrese el numero de anos del prestamo: "))
capital=monto * (1+interes/100)**numeroanios
print('el nuevo capital aplicando una tasa de interes de: ' + str(interes) + ' durante: ' + str(numeroanios) + ' anos, seria de:  ' + str(capital))


