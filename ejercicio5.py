"""
Escriba un programa Python para aceptar un nombre de archivo del usuario e imprimir la extensión de ese
nombre de archivo de muestra: abc. java
Salida: java

"""

import pathlib

file = input('nombre del archivo')
x = pathlib.Path(file).suffix
print(x)
