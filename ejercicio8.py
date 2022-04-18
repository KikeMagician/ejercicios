"""
Escriba un programa en Python para imprimir el calendario de un mes y año determinados. ingresa año y mes
"""

import calendar

anio = int(input('anio'))
mes = int(input('mes (numero)'))
print(calendar.month(anio, mes))
