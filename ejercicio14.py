"""
Escribir un programa de Python para concatenar N cadenas

"""
a = list()
agregar = 0

while agregar == 0:
    x = input('ingrese datos')
    a.append(x)
    agregar = int(input('continuar = 0, terminar = 1'))

l = " ".join(a)
print(l)

