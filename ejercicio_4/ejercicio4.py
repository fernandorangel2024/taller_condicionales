# Programa que calcula el IMC de una persona y determina el diagnóstico correspondiente
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

#   prossesing
imc = peso / altura ** 2

# Mostrar el resultado del IMC
print("Tu IMC es:", round(imc, 2))

# output
if imc < 16:
    print("Criterio de ingreso en hospital.")
elif 16 <= imc < 17:
    print("Infrapeso")
elif 17 <= imc < 18:
    print("Bajo peso")
elif 18 <= imc <= 25:
    print("Peso normal (saludable)")
else:
    print("El diagnóstico para este IMC no está contemplado en el programa.")