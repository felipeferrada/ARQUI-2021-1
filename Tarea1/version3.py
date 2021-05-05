
def valorNum(caracter):
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
    else:
        return int(caracter)

    return valor

def valorChar(num):
    equi_minus = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
        "16": "g",
        "17": "h",
        "18": "i",
        "19": "j",
        "20": "k",
        "21": "l",
        "22": "m",
        "23": "n",
        "24": "o",
        "25": "p",
        "26": "q",
        "27": "r",
        "28": "s",
        "29": "t",
        "30": "u",
        "31": "v",
        "32": "w",
        "33": "x",
        "34": "y",
        "35": "z"
    }
    equi_mayus = {
        "36": "A",
        "37": "B",
        "38": "C",
        "39": "D",
        "40": "E",
        "41": "F",
        "42": "G",
        "43": "H",
        "44": "I",
        "45": "J",
        "46": "K",
        "47": "L",
        "48": "M",
        "49": "N",
        "50": "O",
        "51": "P",
        "52": "Q",
        "53": "R",
        "54": "S",
        "55": "T",
        "56": "U",
        "57": "V",
        "58": "W",
        "59": "X",
        "60": "Y",
        "61": "Z"
    }
    equi_symbols = {
        "62": "+",
        "63": "?"
    }
    valor = str(num)

    if valor in equi_mayus:
        return equi_mayus[valor]

    elif valor in equi_minus:
        return equi_minus[valor]

    elif valor in equi_symbols:
        return equi_symbols[valor]
    else:
        return valor

"""
numero: str
suBase: int
"""
def pasarADecimal(numero, suBase):
    lista = []
    for char in numero:
        lista.append(char)
    lista.reverse()

    decimal = 0
    count = 0

    for n in lista:
        valor = valorNum(n)
        exponente = suBase ** count
        valorEqui = exponente * valor
        decimal += valorEqui
        count += 1

    return str(decimal)

"""
numero: int
baseObjetivo: int
"""
def pasarABaseX(numero, baseObjetivo):
    num = ""

    while numero > 0:
        resto = numero % baseObjetivo
        valorEqui = valorChar(resto)
        num = valorEqui + num
        numero = numero // baseObjetivo

    return num

def pasarNumeroABinario(numero):
    binario = pasarABaseX(int(numero), 2)
    return binario

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def pasarNumericaABCD(numero, suBase):
    enDecimal = pasarADecimal(numero, suBase)
    lista = []
    BCD = ""
    for char in enDecimal:
        lista.append(char)
    for x in lista:
        BCD += pasarNumeroABinario(x) 
    return BCD

def pasarBCDANumerica(numero, baseObjetivo):
    enDecimal = pasarADecimal(numero, 2)
    enBaseObjetivo = pasarABaseX(int(enDecimal), baseObjetivo)

    return enBaseObjetivo

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


basesPosibles = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
"11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
"21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
"31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
"51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
"61", "62", "63", "64"]

basesCodigos = ["bcd", "gry", "bd3", "jsn", "par", "pbt", "ham"]
