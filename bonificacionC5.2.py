def poblar(n):
    lista = []
    
    for i in range(n):
        linea = input()
        datos = linea.split(maxsplit=1)
        tupla = tuple(datos)
        lista.append(tupla)
    return lista


def procesarNotas():
    lista = []
    
    while True:
        linea = input()
        if linea == 'FIN':
            return lista
        
        datos = linea.split()
        
        rut, codigo, nota = datos
        tupla = (rut, codigo, float(nota))
        lista.append(tupla)
    return lista


def procesarEstudiantes(listaEstudiantes,notasFinales):
    lista = []
    
    for estudiante in listaEstudiantes:
        sumaNotas = 0
        contador = 0
        
        for tupla in notasFinales:
            if estudiante[0] == tupla[0]:
                sumaNotas += tupla[2]
                contador += 1
                
        promedio = round(sumaNotas / contador ,1)
        tupla = (estudiante[0], estudiante[1], promedio)
        lista.append(tupla)
    
    return sorted(lista)


def procesarAsignaturas(listaAsignaturas,notasFinales):
    lista = []
    
    for asignatura in listaAsignaturas:
        aprobados = 0
        reprobados = 0
        
        for tupla in notasFinales:
            if asignatura[0] == tupla[1]:
                if tupla[2] >= 4:
                    aprobados += 1
                else:
                    reprobados += 1
        
        tupla = (asignatura[0], asignatura[1], aprobados, reprobados)
        lista.append(tupla)
    
    return sorted(lista)
    


cantEstudiantes = int(input())
listaEstudiantes = poblar(cantEstudiantes)

cantAsignaturas = int(input())
listaAsignaturas = poblar(cantAsignaturas)

notasFinales = procesarNotas()

resumenEstudiantes = procesarEstudiantes(listaEstudiantes,notasFinales)
resumenAsignaturas = procesarAsignaturas(listaAsignaturas,notasFinales)

print(f'LISTA DE ESTUDIANTES - TOTAL TUPLAS = {len(listaEstudiantes)}\n')
for est in listaEstudiantes:
    print(est)

print(f'\nLISTA DE ASIGNATURAS - TOTAL TUPLAS = {len(listaAsignaturas)}\n')
for asig in listaAsignaturas:
    print(asig)
    
print('\nREPORTE ESTUDIANTES ORDENADOS POR RUT\n')
print('    RUT                 NOMBRE                 PROMEDIO')
print('========================================================')    
    

for rut, nombre, promedio in resumenEstudiantes:
    promedio = str(promedio)
    print(f' {rut}{nombre.rjust(31)}{promedio.rjust(11)}')

print('\nREPORTE ASIGNATURA ORDENADAS POR CÓDIGO\n')

print('    CODIGO                            NOMBRE               APROBADOS REPROBADOS')
print('================================================================================')

for codigo, nombre, aprobados, reprobados in resumenAsignaturas:
    aprobados = str(aprobados)
    reprobados = str(reprobados)
    print(f'{codigo.rjust(11)}{nombre.rjust(46)}{aprobados.center(21)}{reprobados}')
