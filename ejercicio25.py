"""
Escriba un programa de Python para imprimir el número de números primos que son menores o iguales que un entero dado
"""
incio = 1
final = 100
limite = 35
lista_primos = []

for number in range(incio, final + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            lista_primos.append(number)

for x in lista_primos:
    if x < limite:
        print(str(x) + ' Es menor al limite')
    else:
        print('el numero primo ' + str(x) + ' es mayor al limite')
        break
