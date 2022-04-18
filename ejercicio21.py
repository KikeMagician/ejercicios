"""
Escriba un programa de Python para crear todas las cadenas posibles usando 'a', 'e', 'i', 'o', 'u'. Use los caracteres exactamente una vez
si se ponse en 5 solo se puede hacer una sin que se repitan los valores
con dos da el maximo sin que se repitan las combinaciones
"""

from itertools import combinations

x = "aeiou"

y = combinations(x, 2)
z = [' '.join(i) for i in y]

print(z)

