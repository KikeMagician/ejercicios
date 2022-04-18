"""
Escriba un programa de Python para contar el número de cada carácter de un texto dado de un archivo de texto.
"""

x = open("txt.txt")
content = x.read()
chars = str(len(content))
print('Caracteres: ' + chars)
