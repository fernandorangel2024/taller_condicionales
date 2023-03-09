# Pedir al usuario que ingrese los m2 de agua gastados
m2_gastados = float(input("Ingresa el número de m2 de agua gastados: "))

# Calcular el gasto de agua
if m2_gastados <= 50:
    gasto_agua = 10000
elif 50 < m2_gastados <= 200:
    gasto_agua = 10000 + (m2_gastados - 50) * 2000
else:
    gasto_agua = 10000 + 150 * 2000 + (m2_gastados - 200) * 3000

# Mostrar el resultado del gasto de agua
print("El gasto de agua es de:", gasto_agua, "pesos.")