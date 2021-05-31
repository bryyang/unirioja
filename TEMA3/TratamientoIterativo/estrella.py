import turtle # Importar paquete de biblioteca de tortugas
turtle.fillcolor("red") #Color de relleno
turtle.begin_fill()              # Comience a dibujar, similar a comenzar un bolígrafo
count = 1                        # Temporizador para contar el número de grabaciones
while count <= 5:                # Control de tiempos de dibujo
 turtle.forward(100) # Dirección del dibujo del pincel, avanzar una distancia especificada
 turtle.right(144) # Gire a la derecha 144 grados
 count += 1                   # Dibujo de ciclo
  
turtle.end_fill()                # Finaliza el dibujo de la imagen rellena.