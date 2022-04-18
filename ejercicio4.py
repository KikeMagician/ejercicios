"""Escriba un programa Python que acepte una secuencia de números separados por comas del usuario y genere una lista y
 una tupla con esos números
Datos de muestra: 3, 5, 7, 23
Salida:
Lista: ['3', ' 5' , ' 7', ' 23']
Tupla: ('3', ' 5', ' 7', ' 23')#
"""

data = input('numeros')
lists = list(data.split(','))
print(lists)
list2 = tuple(data.split(','))
print(list2)
