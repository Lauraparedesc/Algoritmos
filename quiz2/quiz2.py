#punto 1
import pandas as pd 
print ("Pacientes tratados en Medellín durante 2020 : ")
PacientesTratados = {}
PacientesTratados ['Enero'] = 32121
PacientesTratados ['Febrero'] = 14564
PacientesTratados ['Marzo'] = 65465
PacientesTratados ['Abril'] = 85202
PacientesTratados ['Mayo'] = 93213
PacientesTratados ['Junio'] = 100231
PacientesTratados ['Julio'] = 120213
PacientesTratados ['Agosto'] = 65421
PacientesTratados ['Septiembre'] = 46546
PacientesTratados ['Octubre'] = 46547
PacientesTratados ['Noviembre'] = 84651
PacientesTratados ['Diciembre'] = 140521
seriePacientesTratados = pd.Series(PacientesTratados)
print (seriePacientesTratados)

#punto 2
print ("Cuatrimestres: ")
dicPacientesTratados = {}
dicPacientesTratados ['1er Cuatrimestre'] = sum (seriePacientesTratados['Enero':'Abril'])
dicPacientesTratados ['2do Cuatrimestre'] = sum (seriePacientesTratados['Mayo':'Agosto'])
dicPacientesTratados ['3er Cuatrimestre'] = sum (seriePacientesTratados['Septiembre':'Diciembre'])
seriesPacientesC = pd.Series (dicPacientesTratados)
print(seriesPacientesC)

#punto 3
print("Promedio de pacientes atendidos en el mes: ")
print (sum(seriePacientesTratados)/12)

#punto4
print ("Enfermedades : ")
dicEnfermedadesporDep = {
    'Enfermedad general': [32121,14564,65465,85202,93213,100231],
    'COVID-19': [0,0,223,3453,4543,43643],
    'Traumatismos': [6545,43243,67657,435435,345345,43543],
    'Cáncer': [6541,4334,4323,34545,5454,7675],
}
listaMeses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
dataFrameEnfermedadesporDep = pd.DataFrame(dicEnfermedadesporDep, index = listaMeses)
print (dataFrameEnfermedadesporDep)

#punto 5
from functools import reduce
covid19 = [3453,4543,43643]
promedio = lambda numeros, elemento: numeros + elemento
solucion = reduce (promedio,covid19) / len(covid19)
print (solucion)

#punto 6
print (dataFrameEnfermedadesporDep[['Cáncer']]['Enero':'Marzo'])

#Filter
listaEGeneral = [32121,14564,65465,85202,93213,100231]
mayor = lambda paciente = 0 : paciente > 40000
listaMayor = list (filter(mayor,listaEGeneral))
print(listaMayor)

#Map
listaCancer = [6541,4334,4323,34545,5454,7675]
diez = lambda valor : round(valor*0.1,3)
listaC = list(map(diez,listaCancer))
print (listaC)

#Reduce
from functools import reduce
listaTrauma = [6545,43243,67657,435435,345345,43543]
sumar = lambda acumulador = 0, elemento = 0: acumulador + elemento
resultado = reduce (sumar,listaTrauma)
print (resultado)
