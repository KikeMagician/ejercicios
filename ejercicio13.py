"""
Escriba un programa Python para obtener la línea de comando argumentos
(nombre de la secuencia de comandos, número de argumentos, argumentos) pasados a una secuencia de comandos.
"""

import inspect

def sum(a, b):
    return a + b

print(inspect.signature(sum))