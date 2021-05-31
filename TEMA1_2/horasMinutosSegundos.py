def mod(a,b):
    return a%b

def div(c,d):
    return c/d

cantidad = int (input("Dame segundos: "))

s= 3600
s1 = 60

h= div(cantidad,s)
auxiliar =mod(cantidad,s)
m= div(auxiliar,s1)
s= mod(auxiliar,s1)

print(cantidad, " segundos equivalen a: ",h, " horas, ",m," minutos y ",s," segundos")


