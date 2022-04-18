"""
Escriba un programa Python para imprimir un conjunto que contenga todos los colores de
color_list_1 que no están presentes en color_list_2
"""

color_list_1 = set(["White", "Black", "Red" ])
color_list_2 = set(["Red", "Green"])

print((color_list_1 - color_list_2) - (color_list_2 - color_list_1))