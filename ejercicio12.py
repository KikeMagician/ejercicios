"""
Escriba un programa de Python para calcular el valor futuro de un monto principal específico,
una tasa de interés y un número de años
"""

inv = 10000
interes = 3.5
anios = 7

t = (inv * (interes/100) * anios)
print(t + inv)
