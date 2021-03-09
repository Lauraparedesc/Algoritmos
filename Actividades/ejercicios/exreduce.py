#resta elementos lista
from functools import reduce
lista = [85,22,18,19,14,12,8]
restar = lambda acumulador = 0, elemento = 0: acumulador - elemento
resultado = reduce (restar,lista)
print (resultado)

#devolver frase
palabras = ['Hola','buenos','días']
unir = lambda palabras, frase: palabras+' '+frase
resultado1 = reduce (unir,palabras)
print (resultado1)

#sumatoria y división
numeros = [20,25,18,19,7,12,14]
dividirSuma = lambda numeros, elemento: (numeros + (elemento/2))
resultado2 = reduce (dividirSuma,numeros)
print (resultado2)

#promedio
numeros1 = [20,25,18,19,7,12,14]
promedio = lambda numeros, elemento: numeros + elemento
resultado3 = reduce (promedio,numeros1) / len(numeros1)
print (resultado3)

#multiplicación
numeros2 = [20,25,18,19,7,12,14]
multiplicador = lambda acumulado = 0, elemento = 1: acumulado * elemento
multiplicado = reduce (multiplicador, numeros2)/len (numeros2)
print (multiplicado)