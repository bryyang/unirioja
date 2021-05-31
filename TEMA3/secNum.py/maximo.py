n = int(input("Introduce secuencia de numeros positivos acabada en -1"))

if((n>0) and (n!=-1)):
    maximo = n
    while(n!=-1):
        if(n >= maximo):
            maximo = n
        n = int(input())

    print("El maximo es: ", maximo)
    
else: 
    print("Has introducido un numero negativo")