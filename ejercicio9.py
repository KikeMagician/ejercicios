""""
Escriba un programa en Python para calcular el número de días entre dos fechas.
Fechas de muestra: (2014, 7, 2), (2014, 7, 11)

"""

data1 = (2014, 7, 2)
data2 = (2014, 7, 11)
list = []

dif_anio = str(data1[0] - data2[0])
list.append(dif_anio)
dif_mes = str(data1[1] - data2[1])
list.append(dif_mes)
dif_dia = str(data1[2] - data2[2])
list.append(dif_dia)
print('Diferencias de año: ' + list[0] + ' diferencia meses: ' + list[1] + ' difderencia dias: ' + list[2])
