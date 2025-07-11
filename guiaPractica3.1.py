'''
CLUB DE LECTURA

El club de lectura “Letras Vivas” está formado por personas apasionadas por los libros. Este grupo se reúne mensualmente para compartir experiencias lectoras, recomendar títulos y debatir ideas surgidas a partir de sus lecturas. En cada encuentro, los miembros comentan los libros que han leído, ya sea de manera individual o grupal.

Con el objetivo de fomentar la participación y hacer un seguimiento del progreso lector de cada integrante, el club ha comenzado a registrar información detallada sobre cada libro leído a lo largo del año. Este registro permitirá reconocer el compromiso de los miembros y obtener datos relevantes para elaborar un informe durante la reunión de cierre anual.

Información registrada por libro:

Cada vez que un miembro finaliza un libro, se almacena la siguiente información:

Nombre y primer apellido del miembro que leyó el libro (cadena de texto).

Título del libro leído (cadena de texto).

Cantidad de páginas del libro (número entero positivo).

Calificación asignada por el lector (número entero del 1 al 5, donde 1 es la peor nota y 5 la mejor).

------------------------------------------------------------------------------------------------------------------------------------------------------

Diseña un programa modular en Python que facilite la lectura, gestión 

y análisis de los datos registrados por el club.  El programa debe cumplir 

con las siguientes funcionalidades:

------------------------------------------------------------------------------------------------------------------------------------------------------

Funcionalidad 1: Lectura de datos

Leer múltiples registros, uno por cada libro leído.

Cada registro en una línea independiente incluye: nombre del lector, título del libro, número de páginas y calificación, separados por una coma.

Los registros se deben almacenar como tuplas dentro de una lista.

El nombre del lector y el título del libro deben ser almacenados como cadenas de texto en mayúsculas; la cantidad de páginas y la calificación deben ser almacenados como enteros.

La entrada de datos finaliza cuando se lee la palabra "FIN" como nombre del lector.

Se garantiza que no habrá registros duplicados.

Funcionalidad 2: Mostrar registros

Si se ingresaron datos : imprimir por pantalla la lista completa de registros ingresados, mostrando cada tupla con claridad.
En caso contrario imprimir el mensaje "--- NO SE INGRESARON DATOS ---".
Funcionalidad 3: Libros diferentes leídos

Obtener y mostrar una lista ordenada alfabéticamente con los títulos de libros únicos registrados.
Mostrar también la cantidad total de títulos diferentes leídos.
Funcionalidad 4: Calificaciones por título

Generar una nueva lista de tuplas que contenga, para cada título diferente:
El título del libro.
El total de calificaciones recibidas (cantidad de veces que fue leído).
El promedio de las calificaciones, redondeado a dos decimales.
Mostrar esta lista.
Además, identificar y mostrar el/los libros más leídos (los que aparecen con mayor frecuencia en los registros).
Funcionalidad 5: Lectores y su actividad

Generar una nueva lista de tuplas con:
El nombre de cada lector, ordenado alfabéticamente.
La cantidad de libros que leyó.
El total de páginas que leyó.
Mostrar esta lista.
Mostrar también cuántos miembros diferentes tiene el club.
Identificar y mostrar el/los lectores que leyeron más páginas.
Funcionalidad 6: Libros leídos por cada lector

Generar una nueva lista de tuplas donde:
Cada tupla contenga el nombre del lector ordenado alfabéticamente y una lista de títulos leídos ordenada alfabéticamente.
Mostrar esta lista.
'''
def lecturaDatos():
    lista = []
    while True:
        cadena = input()
        datos = cadena.split(',')
        if datos[0] == 'FIN':
            break
        tupla = (datos[0].upper(), datos[1].upper(), int(datos[2]), int(datos[3]))
        lista.append(tupla)
    return lista

def mostrarDatos(lista):
    print('DATOS LEÍDOS\n============')
    for tupla in lista:
        print(tupla)
    print('\n')

def calcularLibrosUnicos(lista):
    listaLibros = []
    for tupla in lista:
        if tupla[1] not in listaLibros:
            listaLibros.append(tupla[1])
    return sorted(listaLibros)

def mostrarLibrosUnicos(lista):
    print('LISTA DE LIBROS - ORDENADOS POR TÍTULO\n=======================================')
    for libro in lista:
        print(libro)
    print(f'\nTOTAL DE LIBROS DIFERENTES LEÍDOS = {len(lista)}')

def calificacionesPorLibro(lista, listaLibros):
    listaTuplas = []
    for libro in listaLibros:
        cantLecturas = 0
        sumaCalificaciones = 0
        for tupla in lista:
            if tupla[1] == libro:
                cantLecturas += 1
                sumaCalificaciones += tupla[3]
        if cantLecturas > 0:
            promedio = round(sumaCalificaciones / cantLecturas, 2)
            tupla = (libro, cantLecturas, promedio)
            listaTuplas.append(tupla)
    return listaTuplas

def mostrarCalificaciones(listaCalificaciones):
    print('\n\nLISTA DE LIBROS, TOTAL DE LECTORES, PROMEDIO DE CALIFICACIÓN\n=============================================================')
    for tupla in listaCalificaciones:
        print(tupla)
    print()

def librosMasLeidos(listaCalificaciones):
    masLeido = listaCalificaciones[0][1]
    lista = []
    for tupla in listaCalificaciones:
        if tupla[1] > masLeido:
            masLeido = tupla[1]
    for tupla in listaCalificaciones:
        if tupla[1] == masLeido:
            lista.append(tupla[0])
    print('LISTA DE LIBROS MAS LEÍDOS\n==========================')
    for libro in lista:
        print(libro)
    print()

def actividadLectores(lista):
    listaLectores = []
    datosLectores = []
    for tupla in lista:
        if tupla[0] not in listaLectores:
            listaLectores.append(tupla[0])
    for lector in listaLectores:
        totalLibros = 0
        totalPaginas = 0
        for tupla in lista:
            if tupla[0] == lector:
                totalLibros += 1
                totalPaginas += tupla[2]
        tupla = (lector, totalLibros, totalPaginas)
        datosLectores.append(tupla)
    datosLectores.sort()
    print('LECTORES ORDENADOS ALF. + TOTAL LIBROS LEÍDOS + TOTAL DE PÁGINAS\n================================================================')
    mayorPaginas = datosLectores[0][2]
    for tupla in datosLectores:
        print(tupla)
        if tupla[2] > mayorPaginas:
            mayorPaginas = tupla[2]
    print(f'\nTOTAL DE MIEMBROS DEL CLUB = {len(datosLectores)}\n')
    listaMasPaginas = []
    for tupla in datosLectores:
        if tupla[2] == mayorPaginas:
            listaMasPaginas.append(tupla[0])
    print('LECTORES QUE HAN LEÍDO MÁS PÁGINAS\n==================================')
    for lector in listaMasPaginas:
        print(lector)
    print()

def resumenLectores(lista):
    print('LECTORES + LIBROS LEÍDOS ORDENADOS ALF.\n=======================================')
    listaLectores = []
    for tupla in lista:
        if tupla[0] not in listaLectores:
            listaLectores.append(tupla[0])
    listaLectores.sort()
    for lector in listaLectores:
        librosLeidos = []
        for tupla in lista:
            if tupla[0] == lector:
                if tupla[1] not in librosLeidos:
                    librosLeidos.append(tupla[1])
        print(f'{lector} : {sorted(librosLeidos)}')

lista = lecturaDatos()

if not lista:
    print('--- NO SE INGRESARON DATOS ---')
else:
    mostrarDatos(lista)
    listaLibros = calcularLibrosUnicos(lista)
    mostrarLibrosUnicos(listaLibros)
    listaCalificaciones = calificacionesPorLibro(lista, listaLibros)
    mostrarCalificaciones(listaCalificaciones)
    librosMasLeidos(listaCalificaciones)
    actividadLectores(lista)
    resumenLectores(lista)

