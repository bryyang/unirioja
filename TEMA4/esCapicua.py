def esCap(num):
    v = []
    i = 0
    while(num > 0):
        v.append(num%10) 
        num /= 10
        i+=1
    capi = True
    iz=0
    der=i
    while(iz < der and capi == True):
        if(v[iz] != v[der-1]):
            capi = False
        else:
            iz+=1
            der-=1
    return capi 


num = int(input("Introduce numero entero: "))
if(esCap(num)):
    print("Es capicua")
else:
    print("No es capicua")
    

