# Programa para indicar el precio de venta de un artículo dado

precio_costo = float(input("Ingrese el precio de costo del artículo: "))
precio_venta = 0

if precio_costo < 3000:
    precio_venta = precio_costo * 1.15
elif precio_costo >= 3000 and precio_costo <= 6000:
    precio_venta = precio_costo + 500
else:
    precio_venta = precio_costo * 1.25

print("El precio de venta del artículo es: $", precio_venta)