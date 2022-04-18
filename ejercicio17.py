"""
Escriba un programa de Python para ingresar un número, si no es un número genera un mensaje de error.
"""
x = input('ingrese un valor para verificar si es un numero')

y = isinstance(x, (int, float))

if y:
    print('es un numero')
else:
    print('no es numero')
