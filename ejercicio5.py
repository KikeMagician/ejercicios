import pathlib


file = input('nombre del archivo')
x = pathlib.Path(file).suffix
print(x)
