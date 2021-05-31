n = int(input("Introduce secuencia de temperaturas acabado en -1: "))
contador =0
acum = 0
while(n != -1): 
    if(n>95):
        acum += n
        contador += 1
    n = int(input())

print("La media de las temperaturas mayores que 95 son: ", acum/contador )
