"""
Escribir un programa de Python para calcular la suma de todos los
elementos de un contenedor (tupla, lista, conjunto, diccionario).
"""

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
list1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

thisdict = {
  "brand": 1,
  "model": 2,
  "year": 1964
}

y = 0

print(sum(list3))
print(sum(list2))
print(sum(list1))
print(sum(thisdict.values()))
