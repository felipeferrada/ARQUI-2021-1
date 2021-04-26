"""
BCD               # 
Gray              #
Exceso de 3       #  reciben numeros en binario
Johnson           #
Paridad           #
PentaBit          #
Hamming           #

Bases numericas: 1 - 10

Para pasar un número desde cualquier base, a base decimal, tenemos que tener en cuenta el valor numérico de cada una de sus cifras.
Este valor está relacionado con la posición de la cifra y de la base en la que se expresa el número.
La posición más a la DERECHA es la posición cero, y ésta posición va aumentando de 1 en 1 hacia la IZQUIERDA hasta que
se acaba el número.

El valor numérico de cada cifra se calcula multiplicando esa cifra por la base elevada a su posición correspondiente
"""

"""
Devuelve el valor numerico de la letra o caracter correspondiente
"""
def Valor_Num(caracter):
    mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minus = "abcdefghijklmnopqrstuvwxyz"

    if caracter in mayus:
        valor = ord(caracter) - 29
    elif caracter in minus:
        valor = ord(caracter) - 87
    elif caracter == "+":
        valor = 62
    elif caracter == "?":
        valor = 63

    return valor

print(Valor_Num("A"))

"""
Para bases del 1 al 10
"""
def Numerica_a_Dec(num, base):
    numero = str(num)
    lista = []
    for i in numero:
        lista.append(i)
    lista.reverse()
    count = 0
    decimal = 0

    while count < len(lista):
        valor = (int(lista[count])*(base**count))
        decimal = decimal + valor
        count += 1
    return decimal

print(Numerica_a_Dec(6147544303, 8))


def Decimal_a_Num(num, base):
    numero = ""
    while num // base != 0:
        numero = str(num % base) + numero
        num = num // base

    return int(str(num) + numero)

print(Decimal_a_Num(898598, 10))