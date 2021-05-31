c=100
def euros(centimos,c): #He definido una funcion para convertir los centimos a euros
    return centimos / c

min = int(input("Introduce minutos hablados: "))

if min <= 3:
    pago = euros(15,c)
    print("Por ",min, " minutos hablados, pagara ",pago, " euros")
#hola

else:
    pago = euros(15,c) + euros((min-3)*10,c)
    print("Por ",min," minutos hablados, pagara ",pago, "euros")
