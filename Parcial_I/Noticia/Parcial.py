# 2 formula del codigo : 8 + xyw + x + w

# 3 valor n
print('sucesión 1')


def sucesion(n):
    return (1/2**n)


print(sucesion(0))
print(sucesion(1))
print(sucesion(2))
print(sucesion(3))

print('sucesión 2')


def sucesion(n):
    return (2*n)+3


print(sucesion(0))
print(sucesion(1))
print(sucesion(2))
print(sucesion(3))

# 4


def contarPalabrasV1(parrafo):
    '''Esta funcion describe cuantas veces 
        aparace cada palabra en una parrafo
        utilizando la instrucción count
    '''
    dictPalabrasOcurrencias = {}
    listaPalabras = parrafo.split()
    for palabra in listaPalabras:
        dictPalabrasOcurrencias[palabra] = listaPalabras.count(palabra)
    return dictPalabrasOcurrencias


def contarPalabrasV2(parrafo):
    '''Esta funcion describe cuantas veces 
        aparace cada palabra en una parrafo
        utilizando otro for
    '''
    dictPalabrasOcurrencias = {}
    listaPalabras = parrafo.split()
    for palabra in listaPalabras:
        dictPalabrasOcurrencias[palabra] = 0
        for i in range(len(listaPalabras)):
            if palabra == listaPalabras[i]:
                dictPalabrasOcurrencias[palabra] += 1
    return dictPalabrasOcurrencias

import time 
parrafo = '''La justicia sobre la fuerza es la impotencia, la fuerza sin justicia es tiranía.
                Vale más saber alguna cosa de todo que saberlo todo de una sola cosa.
                Dos excesos: excluir la razón, no admitir más que la razón.
                Nuestra naturaleza está en movimiento. El reposo absoluto es la muerte.
                El hombre tiene ilusiones como el pájaro alas. Eso es lo que lo sostiene.
                El hombre está dispuesto siempre a negar todo aquello que no comprende.
                Aquel que duda y no investiga, se torna no sólo infeliz, sino también injusto.
                A fuerza de hablar de amor, uno llega a enamorarse.
                ¿De qué le sirve al hombre ganar el mundo si pierde su alma?'''

inicio = time.time ()
contarPalabrasV1 = parrafo
deltaV1 = time.time() - inicio

inicio = time.time ()
contarPalabrasV2 = parrafo
deltaV2 = time.time() - inicio

print (deltaV1,deltaV2)

#Debido a que mi computador rendodea los valores de tiempo tome como referencia los resultados de tiempo en colab, donde V1:0.692 seg y V2: 0.806 seg.
#V2 resulta más lento debido que para hacer el conteo de palabras necesita un for adicional que contenga la función (len) y en V1 el conteo se reliza simplemente con la función count.