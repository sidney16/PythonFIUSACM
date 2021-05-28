num = int(input("Ingresa un número entero:"))

i = 0
verificar= False
for i2 in range(1,num+1):
    if (num% i2)==0:
       i = i + 1
    if i >= 3:
        verificar=True
        break

if i==2 or verificar==False:
    print ("el número es primo")
else: 
    print ("el número no es primo")