#ESTRUCTURA REPETITIVA
#pesoMedio

print("Edad y peso de 5 personas ") # He tomado datos de 5 personas porque escribir datos de 50 personas es mucho
print("--------------------")

def media(sumatorio,divisor): #He definido una funcion para que el algoritmo sea mas escalable
    return sumatorio / divisor


pNino= 0 
pJoven= 0       # Acumuladores de peso
pAdulto= 0                       
cNino= 0          # Contadores 
cJoven= 0
cAdulto= 0

for i in range(5): 
    
    print ("Toma de datos", i+1) # Dado que el rango empieza en 0 he decidido sumar 1 al iterador para poder empezar en 1
    p= int(input("Dame peso: "))
    e= int(input("Dame edad: "))
    print("----------")
    
    if e<= 15:
        cNino= cNino + 1
        pNino = pNino + p 
    
    elif  16<= e <= 30 :
        cJoven= cJoven + 1
        pJoven = pJoven + p 
    
    else :
        cAdulto= cAdulto + 1
        pAdulto = pAdulto + p


print ('Peso medio de los niños ', media(pNino,cNino)) 
print("-----------------------------")
print ('Peso medio de los Jovenes ', media(pJoven,cJoven)) 
print("----------------------------------")
print ('Peso medio de los Adultos ', media(pAdulto,cAdulto)) 





