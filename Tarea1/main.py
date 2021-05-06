
basesNumericas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
"11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
"21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
"31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
"51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
"61", "62", "63", "64"]

basesCodigos = ["bcd", "gry", "ed3", "jsn", "par", "pbt", "ham"]



entrada = input()
while entrada != "-":

    listaEntrada = entrada.split(" ")

    n_numero = listaEntrada[0]
    b_baseEntrada = listaEntrada[1]
    t_baseATransformar = listaEntrada[2]

    if int(n_numero) not in range(1, 1001):     #if pasarADecimal(n_numero) not in range(1, 1001)
        print("Entrada Invalida")
    

    elif b_baseEntrada in basesNumericas and t_baseATransformar in basesNumericas:
        print("ok")

        if int(b_baseEntrada) not in range(1, 65):
            print("Entrada Invalida")

        if int(t_baseATransformar) not in range(1, 65):
            print("Entrada Invalida")


    elif b_baseEntrada in basesNumericas and t_baseATransformar in basesCodigos:
        print("ok")

        if int(b_baseEntrada) not in range(1, 65):
            print("Entrada Invalida")
            

    elif b_baseEntrada in basesCodigos and t_baseATransformar in basesNumericas:
        print("ok")

        if int(t_baseATransformar) not in range(1, 65):
            print("Entrada Invalida")


    elif b_baseEntrada in basesCodigos and t_baseATransformar in basesCodigos:
        print("ok")

    else:
        print("Entrada Invalida")

    entrada = input()

