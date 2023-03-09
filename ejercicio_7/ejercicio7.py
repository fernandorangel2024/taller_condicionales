# Pedir los tres números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

# Verificar si la suma de los dos primeros números es igual al tercero
if num1 + num2 == num3:
    print("La suma de los dos primeros números es igual al tercero.")
else:
    print("La suma de los dos primeros números no es igual al tercero.")