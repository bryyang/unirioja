#ESTRUCTURA REPETITIVA
#sumaSerie


csolicita= float(input("dame cantidad solicitada: "))
print("----------------------")
dosisbase= float(input("dame dosisbase: "))
print("----------------------")
ndosis = 0
n = 1
d = 2
factorcorrector = n/d
cantidadtotal= dosisbase*factorcorrector


while cantidadtotal <= csolicita:
    ndosis= ndosis + 1
    n = n+1
    d = 2*d
    factorcorrector = n/d
    dosis = dosisbase*factorcorrector
    cantidadtotal = cantidadtotal+dosis

	
print("Dada la dosisBase : ", dosisbase , " y la cantidad solicitada: ", csolicita, " el numero de dosis: ", ndosis)