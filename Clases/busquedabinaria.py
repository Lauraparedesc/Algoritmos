def busquedaBinaria(lista, encontrar):
    '''Busqueda Binaria
        se ingresa una lista y un valor a encontrar
        y entonces se devuelve si lo encontró o no
    '''
    isInList = False
    lista.sort()
    izq = 0
    der = len(lista)-1
    while izq <= der and isInList == False:
        print (lista)
        medio = (izq + der)//2
        print('calculo medio',(izq + der)//2)
        print (f'Valor izquierda : {izq}, Valor medio : {medio} ,Valor derecha : {der}')
        #import pdb;pdb.set_encontrar: 
        if lista[medio] == encontrar:
            isInList = True
            return True
        elif lista[medio] > encontrar: 
            der = medio - 1
        else:
            izq = medio + 1
    return isInList 

listaEntrada = [2,12,34,5,11,59,4,3,1]
valorEncontrar = int(input('ingrese un número : '))
print(busquedaBinaria(listaEntrada, valorEncontrar))