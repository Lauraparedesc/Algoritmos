import time
import ordenamiento_Burbuja as ob
import ordenamiento_insercion as oi
import random as r

lista = []
for i in range (9900):
    lista.append(r.randint(1,10000))
listaCopia = lista.copy()
listaCopia2 = lista.copy()
#inicio
inicio = time.time()
#instrucciones
ob.ordenamientoBurbuja(lista)
#delta
deltaOb = time.time() - inicio


#inicio2
inicio = time.time()
#instrucciones2
oi.ordenamientoInsercion(listaCopia2)
#delta2
deltaOi = time.time() - inicio

#inicio
inicio = time.time()
#instrucciones
listaCopia.sort()
#delta
deltaSort = time.time()-inicio
print(deltaSort)
print(deltaOb)
print(deltaOi)
print(deltaSort >= deltaOb)
print(deltaSort >= deltaOi)