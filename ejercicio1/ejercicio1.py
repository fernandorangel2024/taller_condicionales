# Programa que pide al usuario las coordenadas de un punto y muestra en qué cuadrante se encuentra.
x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))

# Verifico en qué cuadrante se encuentra el punto
if x > 0 and y > 0:
    print("El punto se encuentra en el primer cuadrante.")
elif x < 0 and y > 0:
    print("El punto se encuentra en el segundo cuadrante.")
elif x < 0 and y < 0:
    print("El punto se encuentra en el tercer cuadrante.")
elif x > 0 and y < 0:
    print("El punto se encuentra en el cuarto cuadrante.")
elif x == 0 and y == 0:
    print("El punto se encuentra en el origen.")
elif x == 0 and y != 0:
    print("El punto se encuentra sobre el eje y.")
else:
    print("El punto se encuentra sobre el eje x.")