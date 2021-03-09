# divisibles por 7
lista = [28,56,70,56,63,25,12]
siete = lambda valor: valor % 7 == 0
listaSiete = list (filter (siete,lista))
print (listaSiete)

#estudiantes
listaName = ['María','Gustavo','Luis','Elena','Juan','Joaquín']
name = lambda name : (len (name) < 5)
listaNameFilter = list (filter(name,listaName))
print (listaNameFilter)

#pares
listaPar = [22,18,15,46,63,5,3,12]
par = lambda valor: valor % 2 == 0
listaParFilter = list (filter(par,listaPar))
print(listaParFilter)

#impares
listaImpar = [22,18,15,52,91]
numeroImpar = lambda impar = 0 : impar % 2 != 0
listaImparFilter = list (filter(numeroImpar,listaImpar))
print(listaImparFilter)

#Name letra E
listaName = ['María','Gustavo','Luis','Elena','Juan','Eduardo']
nameE = lambda name : name[0] ==  'E'
listaNombresFiltrados = list (filter (nameE, listaName))
print (listaNombresFiltrados)

#+18
listaEdad = [18,19,14,13,8,25,45]
mayores18 = lambda edad = 0 : edad >= 18
listaMas18 = list (filter(mayores18,listaEdad))
print(listaMas18)

#odian
listaPalabra = ['Hoy es un buen día','Los gatos odian el agua','El clima es frío','odian fumar']
odian = lambda palabra: 'odian' not in palabra
listaO = list (filter(odian,listaPalabra))
print(listaO)