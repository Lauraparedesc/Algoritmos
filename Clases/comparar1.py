import time
import ordenamiento_Burbuja as ob
import random as r

lista = []
for i in range (12000):
    lista.append(r.randint(1,10000))
listaCopia = lista.copy()
#inicio
inicio = time.time()
#instrucciones
ob.ordenamientoBurbuja(lista)
#delta
deltaOb = time.time() - inicio


#inicio2
inicio = time.time()
#instrucciones2
listaCopia.sort()
#delta2
deltaSort = time.time()-inicio
print(deltaSort)
print(deltaOb)
print(deltaSort > deltaOb)
