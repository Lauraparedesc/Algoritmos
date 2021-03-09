#crear un elemento donde muestre las ventas totales mes a mes
#de una empresa durante 1 año.
import pandas as pd 

dicEarningPerYear = {}
dicEarningPerYear ['Enero'] = 1234124
dicEarningPerYear ['Febrero'] = 1254124
dicEarningPerYear ['Marzo'] = 1237124
dicEarningPerYear ['Abril'] = 1238124
dicEarningPerYear ['Mayo'] = 1234124
dicEarningPerYear ['Junio'] = 1239124
dicEarningPerYear ['Julio'] = 1234154
dicEarningPerYear ['Agosto'] = 1232124
dicEarningPerYear ['Septiembre'] = 1234124
dicEarningPerYear ['Octubre'] = 1237124
dicEarningPerYear ['Noviembre'] = 1234524
dicEarningPerYear ['Diciembre'] = 1234324

serieEarningPerYear = pd.Series(dicEarningPerYear)
print (serieEarningPerYear)

#
print ('primer trimestre')
print (serieEarningPerYear['Enero':'Marzo'])
print ('tercer trimestre')
print (sum(serieEarningPerYear['Julio':'Septiembre']))
dicGananciasTrimestrales = {}
dicGananciasTrimestrales['1er Trimestre'] = sum (serieEarningPerYear['Enero':'Marzo'])
dicGananciasTrimestrales['2do Trimestre'] = sum (serieEarningPerYear['Abril':'Junio'])
dicGananciasTrimestrales['3er Trimestre'] = sum (serieEarningPerYear['Julio':'Septiembre'])
dicGananciasTrimestrales['4to Trimestre'] = sum (serieEarningPerYear['Octubre':'Diciembre'])
seriesGananciasTrimestrales = pd.Series (dicGananciasTrimestrales)
print(seriesGananciasTrimestrales)
print(sum(serieEarningPerYear))
#Ganancias por mes por Departamento Antioquia, Amazones, Cundinamarca
dicGananciasPorDepartamento = {
    'Antioquia': [124343,3554354,453435,45314,435453,543445],
    'Amazonas': [124343,3554354,453435,45314,435453,543445],
    'Cundinamarca': [124343,3554354,453435,45314,435453,543445],
}
listaMeses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
dataFrameGananciasPorDepartamento = pd.DataFrame(dicGananciasPorDepartamento, index = listaMeses)
print (dataFrameGananciasPorDepartamento)

print (dataFrameGananciasPorDepartamento[['Antioquia','Amazonas']]['Febrero':'Abril'])
