"""
Escriba un programa de Python para imprimir todos los números pares de una lista de números dada en el mismo orden
 y detenga la impresión si aparece algún número después de 237
"""

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
for x in numbers:
    y = x % 2
    if x == 237:
        print('A partir de este numero no se puede serguir imprimiendo')
        break
    elif y != 0:
        pass

    else:
        print(x)
