'''
Sentencias de Control en Python
Mejorar el sistema de autenticación usando la sentencia if-elsif-else
'''

#Escribe tu codigo aqui:
print('*** Sistema de Autenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario = input('Ingresa tu usuario: ')
password = input('Ingresa tu password: ')

if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
    print('Bienvenido al Sistema')
elif usuario == USUARIO_VALIDO:
    print('Password incorrecto, favor de corregirlo!')
elif password == PASSWORD_VALIDO:
    print('Usuario incorrecto, favor de corregirlo!')
else:
    print('Usuario y password incorrectos, favor de corregirlos!')
  
