#ESTRUCTURA REPETITIVA
#sumaSerie
#@author: brfreire

print("CONVERTIDOR DE MINÚSCULA A MAYÚSCULA: ")

print("---------------")

letra= str(input("Introduce una minúscula : "))
'''#Estuve buscando por stackOverflow y solo averigue la manera de convertir una letra a su respectivo codigo ASCII.
 Sin embargo, cuando quiero invertir la accion para imprimir la mayuscula me sale en la terminal que tengo un error de tipo de variable.
 De manera que, he tenido que recurrir al uso del metodo capitalize(), el cual devuelve una copia de la cadena , con la primera letra en mayúsculas.'''

mayuscula= letra.capitalize() 


print("----------------")
print("Su mayúscula es ", mayuscula)



