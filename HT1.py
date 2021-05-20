peso = float(input("Ingresa tu peso en kilogramos:"))
altura = float(input("Ingresa tu altura en metros:"))


imc = round(peso / pow (altura, 2) , 2)

print("Tu índice de masa corporal es ", imc)