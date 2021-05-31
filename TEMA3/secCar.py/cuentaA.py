'''Especificación:

    Interfaz:

        Entrada: entrada secuencial de caracteres acabada en un punto.

        Salida: entero num_a

    Efecto:

        Condiciones de entrada: {...}

        Efecto producido: num_a es el número de aes de la secuencia de entrada

algoritmo contar_a

variables

    entero num_a

    caracter c'''

c = str(input("Introduce texto acabado en punto: "))

num_a=0


while(c!='.'):
    if(c == 'a'):
        num_a+=1
    c = str(input())

print("a ha aparecido, ", num_a, " veces")

