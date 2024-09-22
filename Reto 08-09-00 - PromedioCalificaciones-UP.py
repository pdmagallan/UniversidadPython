'''
Promedio de calificaciones

Crea un programa para realizar el calculo promedio de calificaciones
El programa debe solicitar el numero de calificacionesa utilizar para
obtener el promedio.
Luego se debe solicitar cada calificacion al usuario.
Posteriormente realizar la suma de todas las calificaciones y 
finalmente mandar a imprimir el promedio.
'''

print('*** Promedio de Calificaciones ***')

total_calificaciones = int(input('Proporciona el numero de calificaciones a evaluar: '))
calificaciones = []

# iterar las calificaciones
for indice in range(total_calificaciones):
    calificacion = float(input(f'Calificación[{indice}] = '))
    calificaciones.append(calificacion)

# Imprimimos las calificaciones proporcionadas
print(f'\nLas calificaciones proporcionadas son: {calificaciones}')

# Calculamos el promedio de las calificaciones
# sum(iterable)
suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / total_calificaciones
print(f'\nPromedio de las calificaciones: {promedio:.2f}')
