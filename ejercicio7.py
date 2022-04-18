""""
Escriba un programa de Python que acepte un número entero (n) y calcula el valor de n+nn+nnn
El valor de muestra de n es 5

"""

num = input('ingrese un numerop entero')

uno = int(str(num))
dos = int(str(num)+str(num))
tres = int(str(num)+str(num)+str(num))

num = uno + dos + tres
print(num)
