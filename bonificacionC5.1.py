def poblar():
    lista = []
    
    while True:
        linea = input()
        cadenas = linea.split()
        
        for dato in cadenas:
            if dato == 'FIN':
                return lista
                
            if dato.isdigit():
                if int(dato) > 0 and dato not in lista:
                    lista.append(dato)
                

def transformarLista(lista):
    listaEnt = []
    
    for num in lista:
        listaEnt.append(int(num))
    return listaEnt


def esPrimo(num):
    if num < 2:
        return False
        
    tope = int(num ** 0.5)
    for i in range(2, tope + 1):
        if num % i == 0:
            return False
    return True


def encontrarPrimos(lista):
    primos = []
    
    for num in lista:
        if esPrimo(num):
            primos.append(num)
    return sorted(primos)


def primoAntecesor(num):
    primo = None
    
    for i in range(num - 1, 1, -1):
        if esPrimo(i):
            primo = i
            break
    return primo


def primoSucesor(num):

    i = num + 1
    while True:
        if esPrimo(i):
            return i
        i += 1
        

def esPrimoEquilibrado(num):
    if not esPrimo(num):
        return False
    
    anterior = primoAntecesor(num)
    siguiente = primoSucesor(num)
    
    
    if anterior is not None and siguiente is not None:
        return (anterior + siguiente)/2 == num
    return False


def encontrarPrimosEquilibrados(lista):
    equilibrados = []
    
    for num in lista:
        if esPrimoEquilibrado(num):
            primoAnt = primoAntecesor(num)
            primoSig = primoSucesor(num)
            tupla = (num, primoAnt, primoSig)
            equilibrados.append(tupla)
    
    return sorted(equilibrados,reverse=True)   




lista = poblar()
listaEntera = transformarLista(lista)
listaPrimos = encontrarPrimos(listaEntera)
primosEquilibrados = encontrarPrimosEquilibrados(listaEntera)

if not lista:
    print('''============================================================
NO SE INGRESARON NÚMEROS ENTEROS POSITIVO MAYORES A CERO
============================================================''')

else:
    print(f'============================================================\nTOTAL DE NÚMEROS ENTEROS POSITIVOS MAYORES A CERO LEÍDOS = {len(lista)}')
    print(f'LISTA DE NÚMEROS ENTEROS POSITIVOS MAYORES A CERO LEÍDOS\n{lista}\n============================================================')
    
    if not listaPrimos:
        print('''============================================================
NO SE ENCONTRARON NÚMEROS PRIMOS
============================================================''')
    
    
    else:
        print(f'============================================================\nTOTAL DE NÚMEROS PRIMOS  = {len(listaPrimos)}')
        print(f'LISTA DE NÚMEROS PRIMOS\n{listaPrimos}\n============================================================')
        
        if primosEquilibrados:
            print(f'============================================================\nTOTAL DE TUPLAS DE PRIMOS EQUILIBRADOS = {len(primosEquilibrados)}')
            print(f'LISTA DE TUPLAS DE PRIMOS EQUILIBRADOS\n{primosEquilibrados}\n============================================================')
        else:
            print('''============================================================
NO SE ENCONTRARON NÚMEROS PRIMOS EQUILIBRADOS
============================================================''')




        