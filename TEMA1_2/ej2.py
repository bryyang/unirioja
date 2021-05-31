#EJERCICIOS PRACTICAS 1 SESION


print("Calculadora de raíces del polinomio")
print("-----------------------")
print("a*x**2 + b*x + c")
print("-------------------")
a= int(input("Dame el coeficiente a= "))
print("----------------------")
b=int(input("Dame el coeficiente b= "))
print("---------------------")
c=int(input("Dame el coeficiente c= "))
print("--------------------")

r = (b**2 - 4*a*c)



if r >= 0: 
    raiz1 = (-b+(b**2 - 4*a*c)**(1/2))/(2*a)
    raiz2 = (-b+(b**2 - 4*a*c)**(1/2))/(2*a)
    print("las raices de la ecuacion ","(", a, ")"   ,"x**2", "+" ,"(", b ,")","x", "+","(", c, ")" " sus raices son ", "x1=", raiz1, "x2=", raiz2)  
else:
    print("No existe la raíz de un numero negativo")

    

