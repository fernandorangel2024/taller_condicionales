# Definición de variables
ingresos = float(input("Ingrese sus ingresos mensuales: "))
deuda = input("¿Tiene alguna deuda actualmente? (Sí/No): ")

# Verificación de elegibilidad
if ingresos >= 945200 and deuda.lower() == "no":
    print("Felicidades, usted es elegible para un préstamo bancario.")
    # Solicitud del monto del préstamo
    monto = float(input("¿Cuánto dinero desea solicitar en préstamo? "))
    print("Su préstamo de $", monto, " ha sido aprobado.")
else:
    print("Lo siento, usted no cumple con los requisitos para obtener un préstamo bancario.")