# Función CalcularAreaPerimetro: recibe el radio de una circunferencia y
# devuelve el área y el perímetro.
# Parámetros de entrada: radio (real)
# Valores de salida: área y perímetro (real)
import math #libreria math
def CalcularAreaPerimetro(radio):
	area = math.pi * radio ** 2;
	perimetro = 2 * math.pi * radio;
	return area,perimetro

radio = float(input("Introduce el radio:"))
area,perimetro = CalcularAreaPerimetro(radio)
print("Área:",area)
print("Perímetro:",perimetro)
