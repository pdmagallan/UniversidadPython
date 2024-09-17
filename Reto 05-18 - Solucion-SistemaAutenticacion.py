'''
Operadores en Python
Sistema de Autenticación
Crea un programa para validar el usuario y password proporcionados por el usuario.
Crea 2 constantes con los valores correctos y posteriormente compara que el usuario y password proporcionados por el usuario sean válidos.
Debe solicitar el usuario y el password al usuario y si son iguales que los valores correctos almacenados en las constantes debe imprimir True, de lo contrario debe mandar a imprimir False.
'''

#Escribe tu codigo aqui:
print('*** Sistema de Autenticación ***')
USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario_ingresado = input('Cual es tu usuario?')
password_ingresado = input('Cual es tu password?')

son_datos_correctos = (usuario_ingresado.strip() == USUARIO_VALIDO
                      and password_ingresado.strip() == PASSWORD_VALIDO)

print(f'Datos son correctos? {son_datos_correctos}')
