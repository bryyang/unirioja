#EJERCICIOS PRACTICAS 1 SESION


print("Calculadora de una ecuación de 3* grado para un valor concreto")
print("---------------------------------")
print("Dada la ecuación ax**3 + bx**2 + cx + d ")
print("----------------------------------")
a= int(input("Introduce valor para a: "))
b= int(input("Introduce valor para b: "))
c= int(input("Introduce valor para c: "))
d= int(input("Introduce valor para d: "))
x= int(input("Introduce valor para x: "))

f =  a*x**3 + b*x**2 + c*x + d

print("--------------------")
print("la solución de la ecuación: ", "(", a,")","x**3 + ",  "(", b,")","x**2 + ",  "(", c,")", "x + ","(",  d, ")", " para el valor de x=",x,  "es : ", f )



