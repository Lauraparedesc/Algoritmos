#Exponente n de un # dado
exponente = lambda base = 0, exponente = 0 : base**exponente
resultado = exponente (5,2)
print (resultado)

#string
string = lambda cantidad = 0 : print ('♡'*cantidad)
string (60)

#maximo #
listaEdades1 = [18,12,14,13,12,20]
listaEdades2 = [19,47,75,14,12,22]

lambdamaximos = lambda x = [], y = []: print (max(x),max(y))
lambdamaximos (listaEdades1, listaEdades2)

#V o F par
numeroPar = lambda par = 0 : par % 2 == 0
print(numeroPar(23))
print(numeroPar(12))

#V o F impar
numeroImpar = lambda impar = 0 : impar % 2 != 0
print(numeroImpar(23))
print(numeroImpar(12))

#union 2 palabras
unirP = lambda word1 , word2 : word1 + ' ' + word2
print (unirP('Soy','programador')) 

#saludo
preguntaNombre = 'Ingrese su nombre por favor : '
nombre = input(preguntaNombre)
saludar = lambda name = '' : print (f'Bienvenid@ {name}, disfruta el programa')
saludar(nombre)

#Letras
palabraX = 'Blessed'
lenPalabra  = lambda palabra : len (palabra)
print (lenPalabra(palabraX))

#¿?
showLen = lambda funcion, palabra : print (funcion(palabra))
showLen(lenPalabra, palabraX)

#Triangulo
calcularAreaTriangulo = lambda base = 0, altura = 0: base*altura/2
print(calcularAreaTriangulo(5,8))

#IMC
imc = lambda peso = 0, altura = 1: round(peso/altura**2,3)
print (imc(48,1.58))

