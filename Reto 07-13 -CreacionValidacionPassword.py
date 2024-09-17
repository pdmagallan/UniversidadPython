'''
Creación y validación de password
Crear un programa para solicitar la validación al momento de crear un valor de un password.
La contraseña debe tener al menos 6 caraceres.
En caso de no cumplir con esta condición el programa debe volver a solicitar un nuevo valor hasta que se cumpla con la condición.
Si el valor proporcionado es válido, se debe imprimir "Password Válido" y debe terminar la ejecución del sistema.
'''

#Escribe tu codigo aqui:
print('*** Creación y Validación de un Password ***')

password = input('Ingresa un password (debe tener al menos 6 caracteres: ')

# Validar el password
while len(password) < 6:
    print('El password no cumple con los requisitos. Debe tener al menos 6 caracteres')
    password = input('Ingresa un nuevo valor de password: ')
else:
    print('El valor de password es válido')
