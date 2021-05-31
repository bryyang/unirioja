#ESTRUCTURA REPETITIVA
#sumaSerie


dosisbase= float(input("dame dosisBase: "))
print("----------------------")
ndosis= int(input("dame numero de dosis: "))
print("----------------------")
cantidadtotal = 0
n = 1
d = 2

for i in range(ndosis):
	factorcorrector = n/d
	dosis = dosisbase*factorcorrector
	cantidadtotal = cantidadtotal+dosis
	n = n+1
	d = 2*d
	
print("Dada la dosisBase : ", dosisbase , " y el numero de dosis suministrada: ", ndosis, " la cantidad total es: ", cantidadtotal)