def obtenerMultiplicador(categoria,destino):
    
    if destino == 3:
        if categoria == "LATAM":
            return 5
        elif categoria == "GOLD":
            return 6
        elif categoria == "GOLD PLUS":
            return 7
        elif categoria == "PLATINUM":
            return 9
        elif categoria == "BLACK":
            return 10
        elif categoria == "BLACK SIGNATURE":
            return 11
    
    else:
        if categoria == "LATAM":
            return 3
        elif categoria == "GOLD":
            return 4
        elif categoria == "GOLD PLUS":
            return 5
        elif categoria == "PLATINUM":
            return 7
        elif categoria == "BLACK":
            return 8
        elif categoria == "BLACK SIGNATURE":
            return 9


def procesarSocio():
    
    rut = input()
    categoria = input()
    
    millas = 0
    totalDolares = 0
    viajesNacionales = 0
    viajesSudamerica = 0
    viajesInternacionales = 0
    
    while True:
        codigoReserva = input()
        if codigoReserva == 'FINISH':
            break
        
        destino = int(input()) #(1) nacional, (2) sudamerica, (3) internacional
        precio = int(input())
        
        totalDolares += precio
        
        if destino == 1:
            viajesNacionales += 1
        elif destino == 2:
            viajesSudamerica += 1
        elif destino == 3:
            viajesInternacionales += 1
        
        multiplicador = obtenerMultiplicador(categoria,destino)
        millas += precio * multiplicador
        
    tupla = (rut, categoria, millas, totalDolares, viajesNacionales, viajesSudamerica, viajesInternacionales)
    
    return tupla


def poblarSocios(n):
    lista = []
    
    for elementos in range(n):
        socio = procesarSocio()
        lista.append(socio)
    
    return sorted(lista)
    
    
def imprimirLista(lista):
    for elementos in lista:
        print(elementos)
        

def calcularMayorMilla(lista):
    mayorMilla = lista[0][2]
    menorMilla = lista[0][2]
    socioMayorMilla = lista[0][0]
    listaMayorMilla = []
    listaMenorMilla = []
    socioMenorMilla = lista[0][0]
    
    
    for tuplas in lista:
        if tuplas[2] > mayorMilla:
            mayorMilla = tuplas[2]
            socioMayorMilla = tuplas[0]
        
        if tuplas[2] < menorMilla:
            menorMilla = tuplas[2]
            socioMenorMilla = tuplas[0]
    
    for tuplas in lista:
        if tuplas[2] == mayorMilla:
            listaMayorMilla.append(tuplas[0])
        
        if tuplas[2] == menorMilla:
            listaMenorMilla.append(tuplas[0])
            
    return mayorMilla, listaMayorMilla, menorMilla, listaMenorMilla
    

def calcularCategoria(lista):
    
    listaCategorias = [[],[],[],[],[],[]]
    
    contLatam = 0
    
    contGold =0
    
    contGoldPlus = 0
    
    contPlatinum = 0
    
    contBlack = 0
    
    contBlackSignature = 0
    
    for tuplas in lista:
        
        if tuplas[1] == 'LATAM':
            contLatam += 1
            listaCategorias[0].append(tuplas[2])
        
        elif tuplas[1] == 'GOLD':
            contGold += 1
            listaCategorias[1].append(tuplas[2])
        
        elif tuplas[1] == 'GOLD PLUS':
            contGoldPlus += 1
            listaCategorias[2].append(tuplas[2])
        
        elif tuplas[1] == 'PLATINUM':
            contPlatinum += 1
            listaCategorias[3].append(tuplas[2])
        
        elif tuplas[1] == 'BLACK':
            contBlack += 1
            listaCategorias[4].append(tuplas[2])
            
        elif tuplas[1] == 'BLACK SIGNATURE':
            contBlackSignature += 1
            listaCategorias[5].append(tuplas[2])
    
    return listaCategorias


def resumenCategoria(lista):
    
    if lista[0]:
        suma = sum(lista[0])
        largo = len(lista[0])
        promedio = round(suma / largo)
        
        print(f'LATAM - {largo} socios - total millas = {suma} ==> promedio millas = {promedio}')
    else:
        print('LATAM - NO hay socios en esta categoria')

    if lista[1]:
        suma = sum(lista[1])
        largo = len(lista[1])
        promedio = round(suma / largo)
        
        print(f'GOLD - {largo} socios - total millas = {suma} ==> promedio millas = {promedio}')
    else:
        print('GOLD - NO hay socios en esta categoria')
    
    if lista[2]:
        suma = sum(lista[2])
        largo = len(lista[2])
        promedio = round(suma / largo)
        
        print(f'GOLD PLUS - {largo} socios - total millas = {suma} ==> promedio millas = {promedio}')
    else:
        print('GOLD PLUS - NO hay socios en esta categoria')
    
    if lista[3]:
        suma = sum(lista[3])
        largo = len(lista[3])
        promedio = round(suma / largo)
        
        print(f'PLATINUM - {largo} socios - total millas = {suma} ==> promedio millas = {promedio}')
    else:
        print('PLATINUM - NO hay socios en esta categoria')
    
    if lista[4]:
        suma = sum(lista[4])
        largo = len(lista[4])
        promedio = round(suma / largo)
        
        print(f'BLACK - {largo} socios - total millas = {suma} ==> promedio millas = {promedio}')
    else:
        print('BLACK - NO hay socios en esta categoria')
    
    if lista[5]:
        suma = sum(lista[5])
        largo = len(lista[5])
        promedio = round(suma / largo)
        
        print(f'BLACK SIGNATURE - {largo} socios - total millas = {suma} ==> promedio millas = {promedio}')
    else:
        print('BLACK SIGNATURE - NO hay socios en esta categoria')
    
    
def calcularViajes(lista):
    
    viajesInternacionales = []
    viajesSudamerica = []
    viajesNacionales = []
    
    for tuplas in lista:
        viajesInternacionales.append(tuplas[-1])
        viajesSudamerica.append(tuplas[-2])
        viajesNacionales.append(tuplas[-3])
    
    sumaInternacionales = sum(viajesInternacionales)
    sumaSudamerica = sum(viajesSudamerica)
    sumaNacionales = sum(viajesNacionales)
    
    return sumaNacionales, sumaSudamerica, sumaInternacionales
    

def imprimirViajes(n,s,i):
    if n == 0:
        print(f'tipo 1 : NO hay viajes de este tipo')
    else:
        print(f'tipo 1 : {n} viaje(s)')
        
    if s == 0:
        print(f'tipo 2 : NO hay viajes de este tipo')
    else:
        print(f'tipo 2 : {s} viaje(s)')
        
    if i == 0:
        print(f'tipo 3 : NO hay viajes de este tipo')
    else:
        print(f'tipo 3 : {i} viaje(s)')
    

def calcularMaximoGastado(listaSocios):
    maximo = listaSocios[0][3]
    listaMaximo = []
    
    for tuplas in listaSocios:
        if tuplas[3] > maximo:
            maximo = tuplas[3]
    
    for tuplas in listaSocios:
        if tuplas[3] == maximo:
            listaMaximo.append(tuplas[0])
            
    return maximo, listaMaximo

 
def calcularSocioMasViajes(listaSocios):
    listaViajes = []
    listaRutViajes = []
    
    for socio in listaSocios:
        total = socio[4] + socio[5] + socio[6]
        listaViajes.append(total)
        listaRutViajes.append(socio[0])
        
    maximosViajes = max(listaViajes)
    socioMaximosViajes = []
    
    i = 0
    while i < len(listaViajes):
        if listaViajes[i] == maximosViajes:
            socioMaximosViajes.append(listaRutViajes[i])
        i += 1
    
    
    return maximosViajes, socioMaximosViajes
    
    
    
cantSocios = int(input())
listaSocios = poblarSocios(cantSocios)

print(f'Se procesarán {len(listaSocios)} socios LATAM pass.')
print()
print('==============================================')
print('LISTA DE TUPLAS DATOS SOCIOS ORDENADAS POR RUT')
print('==============================================')
print()
print('RUT - CATEGORIA - TOTAL MILLAS- DOLARES GASTADOS - TOTAL NAC. - TOTAL SUDAM. - TOTAL INTERN.')

imprimirLista(listaSocios)
socioMayorMillas, rutSocioMayorMillas, socioMenorMillas, rutSocioMenorMillas = calcularMayorMilla(listaSocios)

print()
print(f'Los siguientes socios acumularon la mayor cantidad de millas = {socioMayorMillas}')
print(f'Lista Rut = {rutSocioMayorMillas}')

print()
print(f'Los siguientes socios acumularon la menor cantidad de millas = {socioMenorMillas}')
print(f'Lista Rut = {rutSocioMenorMillas}')

print()
print('RESUMEN POR CATEGORÍA')
print('=====================')

listaCategoria = calcularCategoria(listaSocios)

resumenCategoria(listaCategoria)

print()
print('RESUMEN POR TIPO DE VIAJE')
print('=========================')

viajesNacionales, viajesSudamerica, viajesInternacionales  = calcularViajes(listaSocios)

imprimirViajes(viajesNacionales, viajesSudamerica, viajesInternacionales)

print()
print('MÁXIMO MONTO DÓLARES GASTADO POR SOCIO')

maximoGastado, socioMaximo = calcularMaximoGastado(listaSocios)

print(f'Máximo monto dólares = US$ {maximoGastado}')
print(f'Lista de socios con máximo monto dólares gastado : {socioMaximo}')

print()

mayorCantViajes, socioMayorViajes = calcularSocioMasViajes(listaSocios)

print('MÁXIMA CANTIDAD DE VIAJES POR SOCIO')
print(f'Máxima cantidad de viajes de socios es: {mayorCantViajes}')
print(f'Lista de socios con máxima cantidad de viajes : {socioMayorViajes}')