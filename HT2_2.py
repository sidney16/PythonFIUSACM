num = int(input("Ingresa un número entero positivo:"))

i = num
cadena = ''
if num >= 0:
    while i >= 0:
        cadena = cadena + str(i) + ','
        i=i-1
    print (cadena)
else:
    print("el número es negativo, ingrese uno positivo")