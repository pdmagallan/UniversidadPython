'''
Sistema Tienda Online
Crear el detalle de un producto de una tienda online.
El detalle del producto debe tener:
*Nombre
*Precio
*Cantidad en el inventario
*Indicar si está disponible
Imprimir por consola el detalle, hacer algunos cambios y mandar a imprimir nuevamente.
'''

#Escribe tu codigo aqui:
print('*** Sistema de Tienda Online ***')

# Definir las variables de un producto
nombre_producto = 'Cámara digital'
precio_producto = 399.99
cantidad_inventario = 20
disponible_entrega = True

# Mostrar información del producto
print('Producto:', nombre_producto)
print('Precio: $', precio_producto)
print('Cantidad en el inventario:', cantidad_inventario)
print('Disponible para entrega:', disponible_entrega)

# Hacemos algunos cambios
precio_producto = 299.99
cantidad_inventario = 10
disponible_entrega = True

# Mostrar información del producto
print()
print('Producto:', nombre_producto)
print('Precio: $', precio_producto)
print('Cantidad en el inventario:', cantidad_inventario)
print('Disponible para entrega:', disponible_entrega)
