'''
Ejercicio Contador de Vocales en Python
Escribe un programa que declare una variable llamada cadena con el valor de "Hola Mundo".

Posteriormente usando un ciclo for, debe contar la cantidad de vocales presentes en la cadena
y finalmente imprimir la cantidad de vocales encontradas (solo el número con la cantidad de 
vocales encontradas es el que se debe imprimir).
'''

# Declarar la variable
cadena = 'Hola Mundo'
contador = 0
# Agregar el ciclo for 
for letra in cadena:
    if letra=='a' or letra=='e'or letra=='i' or letra=='o' or letra=='u' or letra=='A'or letra=='E' or letra=='I' or letra=='O'or letra=='U':
        contador = contador + 1
# Imprimir la cantidad de vocales encontradas en la cadena
print (contador)
