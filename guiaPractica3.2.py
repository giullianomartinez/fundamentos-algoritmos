'''
NÚMEROS HARSHAD & TRIMÓRFICOS
En matemáticas, un número de Harshad, es un entero divisible por la suma de sus dígitos. Estos números fueron definidos por Kaprekar, un matemático indio. La palabra "Harshad" proviene del sánscrito, que significa gran alegría.  

POR EJEMPLO :

El número 5 es un número de Harshad, ya que es divisible por la suma de sus dígitos que es 5.
El número 12 es un número de Harshad, ya que es divisible por la suma de sus dígitos que es 3.
El número 375 es un número de Harshad, ya que es divisible por la suma de sus dígitos que es 15.
Por otra parte, un número X es trimórfico, si al elevarlo al cubo se obtiene un número que termina en X.

POR EJEMPLO :

El número 5 es un número trimórfico, ya que al elevarlo al cubo 53 obtenemos 125 que termina en 5.
El número 99 es un número trimórfico, ya que al elevarlo al cubo 993 obtenemos 970299 que termina en 99.
El número 375 es un número trimórfico, ya que al elevarlo al cubo 3753 obtenemos 52734375 que termina en 375.
Como puedes ver hay números que son de Harshad y Trimórficos simultáneamente, a esos números los llamaremos HARSHTRIMOS.

========================================================================================

Escribe un programa en Python con funciones propias que permita:
Leer líneas con datos, hasta que se detecte la cadena "FIN". Los datos (string) deben ser almacenados en forma independiente en una lista de números SOLAMENTE si son números enteros positivos, MAYORES a 0 y SIN REPETICIONES. 
Mostrar por pantalla la lista de números enteros diferentes y MAYORES a 0 ingresados y su cantidad. Si NO se ingresó ningún número entero positivo y MAYOR a 0, se mostrará el mensaje "NO SE INGRESARON NÚMEROS ENTEROS POSITIVOS MAYORES A 0."
SOLO SI se ingresaron números enteros positivos mayores a 0 (1 o más) :
Para cada número (X) en la lista de números ingresados : 
Mostrar el número procesado (X).
Analizar si el número X es o NO es de Harshad, mostrando el proceso tal como se muestra en los ejemplos de ejecución. 
Analizar si el número es o NO es Trimórfico, mostrando el proceso tal como se muestra en los ejemplos de ejecución. 
Determinar si el número es o NO es HARSHTRIMO. Si el número es HARSHTRIMO se deberá almacenar en una lista de números HARSHTRIMOS.
Al finalizar el procesamiento de todos los números en la lista de números ingresados. 
Si la lista de HARSHTRIMOS obtenida está vacía imprimir por pantalla el mensaje "NO SE ENCONTRARON NÚMEROS HARSHTRIMOS.".
Si la lista de HARSHTRIMOS obtenida tiene datos. Mostrar la lista por pantalla ordenada de MAYOR a MENOR y su cantidad de elementos.
'''
def procesarDatos():
    lista = []
    while True:
        linea = input()
        palabras = linea.split()
        for cad in palabras:
            if cad == 'FIN':
                return lista
            if cad.isdigit():
                num = int(cad)
                if num > 0 and num not in lista:
                    lista.append(num)
    return lista

def mostrarDatos(lista):
    print(f'LISTA NÚMEROS ENTEROS MAYORES A CERO DIFERENTES INGRESADOS = {lista}')
    print(f'TOTAL DE NÚMEROS EN LA LISTA = {len(lista)}\n')

def sumaDigitos(num):
    suma = 0
    for digito in str(num):
        suma += int(digito)
    return suma

def esHarshad(num):
    return num % sumaDigitos(num) == 0

def potencia10SegunLargo(num):
    largoNum = len(str(num))
    potencia = 10 ** largoNum
    return potencia

def esTrimorfico(num):
    cubo = num ** 3
    return cubo % potencia10SegunLargo(num) == num

def esHarshtrimo(num):
    return esHarshad(num) and esTrimorfico(num)

def procesarNumeros(lista):
    print('------------ PROCESAMIENTO DE NÚMEROS EN LISTA ------------\n')    
    listaHT = []
    textoHarsh = ''
    textoTrim = ''
    textoHT = ''
    for num in lista:
        print(f'NÚMERO PROCESADO {num}\n')
        if esHarshad(num):
            textoHarsh = 'SI ES DE HARSHAD'
        else:
            textoHarsh = 'NO ES DE HARSHAD'
        if esTrimorfico(num):
            textoTrim = 'SI ES TRIMÓRFICO'
        else:
            textoTrim = 'NO ES TRIMÓRFICO'
        if esHarshtrimo(num):
            textoHT = 'SI ES HARSHTRIMO'
            listaHT.append(num)
        else:
            textoHT = 'NO ES HARSHTRIMO'
        mod = sumaDigitos(num)
        resto = num % mod
        print(f'''LA SUMA DE DÍGITOS DE {num} = {mod} Y EL RESTO DE {num} % {mod} = {resto}
EN CONCLUSIÓN {num} {textoHarsh}\n''')
        cubo = num ** 3
        termina = cubo % potencia10SegunLargo(num)
        print(f'''{num} ^ 3 = {cubo} Y EL {cubo} TERMINA EN {termina}
EN CONCLUSIÓN {num} {textoTrim}\n''')
        print(f'FINALMENTE {num} {textoHT}')
        print('===========================================================')
    print()
    if listaHT:
        print('------------ FIN PROCESAMIENTO DE NÚMEROS EN LISTA ------------\n')
        listaHT.sort(reverse=True)
        print(f'LISTA DE HARSHTRIMOS ORDENADOS DE MAYOR A MENOR = {listaHT}')
        print(f'LA LISTA TIENE {len(listaHT)} ELEMENTO(S).')
    else:
        print('------------ FIN PROCESAMIENTO DE NÚMEROS EN LISTA ------------\n')
        print('NO SE ENCONTRARON NÚMEROS HARSHTRIMOS.')

lista = procesarDatos()

if not lista:
    print('NO SE INGRESARON NÚMEROS ENTEROS POSITIVOS Y MAYORES A 0.')
else:
    mostrarDatos(lista)
    procesarNumeros(lista)


