def poblar():
    lista = []

    while True:
        linea = input()
        if linea == 'FIN':
            return sorted(lista)

        cadena = linea.split()

        for dato in cadena:
            entero = int(dato)
            if entero > 5 and entero not in lista:
                lista.append(entero)


def sumaDigitosElevados(num):
    suma = 0
    contador = 1

    for digito in str(num):
        suma += int(digito) ** contador
        contador += 1
    return suma


def raizCuarta(num):
    return round(num ** (1/4) ,4)


def distancia(num):
    suma = sumaDigitosElevados(num)

    if suma > num:
        return suma - num
    else:
        return num - suma


def esDinoAmpliado(num):
    return distancia(num) < raizCuarta(num)


def procesarNumeros(lista):
    dinoAmpliados = []

    for num in lista:
        suma = sumaDigitosElevados(num)
        texto = ''

        if esDinoAmpliado(num):
            texto = f'SI es dinoampliado'
            dinoAmpliados.append(num)
        else:
            texto = f'NO es dinoampliado'

        print(f'{num} - suma = {suma} - distancia = {distancia(num)} - raiz = {raizCuarta(num)}. {texto}')

    dinoAmpliados.sort(reverse=True)

    if dinoAmpliados:
        print(f'Lista de numeros dinoampliados = {dinoAmpliados}')
    else:
        print('NO hay numeros dinoampliados')


lista = poblar()

procesarNumeros(lista)
