num = int(input("Ingresa un número entero positivo:"))

i = 1
i2 = 1
cadena = ''
if num >= 0:
    while i <= num:
        while i2 <= i:
            cadena = cadena + '*'
            i2=i2+1
        i=i+1
        i2=1
        print (cadena)
        cadena = ''
else:
    print("el número es negativo, ingrese uno positivo")