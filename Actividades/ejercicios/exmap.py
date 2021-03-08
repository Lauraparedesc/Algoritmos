#cuadrado de cada elemento
listaNumeros = [20,80,41,24,18,12]
cuadrado = lambda valor : valor**2
listaC = list(map(cuadrado,listaNumeros))
print  (listaC)

#dividir por el mayor
mayor = max(listaNumeros)
dividir = lambda valor = 0: round(valor/mayor,2)
listaNormalizada = list (map(dividir, listaNumeros))
print (listaNormalizada)

#reste un # n
n = int (input('ingrese valor a restar : '))
restarN = lambda valor : valor - n
restarNListas = list (map(restarN, listaNumeros))
print (restarNListas)

#sume un # n
n = int (input('ingrese valor a sumar : '))
sumarN = lambda valor : valor + n
sumarNListas = list (map(sumarN, listaNumeros))
print (sumarNListas)

#multiplicación x5
n = 5
multiplicarN = lambda valor : valor * n
multiplicarNListas = list (map(multiplicarN, listaNumeros))
print (multiplicarNListas)
