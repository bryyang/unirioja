num = int(input("Dime un numero entero positivo: "))
divisores = 0
i=1
while(i <= num):
    i = i + 1
    if(num%i==0):
        divisores = divisores + 1



if(divisores <=2):
    print("El numero es primo ")
else:
    print("El numero no es primo ")




 
