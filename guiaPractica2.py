def esNaturalConsecutivo(n):
    a = 1
    while a + (a + 1) <= n:
        if a + (a + 1) == n:
            return True
        a += 1
    return False


def esDeficiente(n):
    sumaDivisores = 0
    for i in range(1, n):
        if n % i == 0:
            sumaDivisores += i
    return sumaDivisores < n


def esTriangular(n):
    i = 0
    while i <= n:
        if i * (i + 1) // 2 == n:
            return True
        if i > n:
            return False
        i += 1
    return False


def contieneDigito2(n):
    while n > 0:
        ultimoDigito = n % 10
        if ultimoDigito == 2:
            return True
        n //= 10
    return False


def calcularPorcentaje(parcial,total):
    if total == 0:
        return 0.0
    return (parcial/total) * 100


def puedeActivarCristal(fragmentosRecolectados,sumaFragmentos,menorFragmento,promedio):
    return esNaturalConsecutivo(fragmentosRecolectados) and esDeficiente(sumaFragmentos) and esTriangular(menorFragmento) and contieneDigito2(promedio)


def main():
    
    numeroCadete = 1
    totalCadetes = 0
    activaronCristal = 0
    noActivaronCristal = 0


    while True:
        nombre = input()
        if nombre == "FIN":
            break
    
        fragmentosRecolectados = int(input())

        i = 0
        menorFragmento = 0
        sumaFragmentos = 0

        while i < fragmentosRecolectados:
            fragmento = int(input())
            sumaFragmentos += fragmento
            
            if i == 0:
                menorFragmento = fragmento
            if fragmento < menorFragmento:
                menorFragmento = fragmento
            i += 1
        promedio = sumaFragmentos // fragmentosRecolectados


        print(f"CADETE #{numeroCadete} --> {nombre}")
        print(f"""TOTAL FRAGMENTOS RECOLECTADOS = {fragmentosRecolectados}
    SUMA VALORES DE FRAGMENTOS RECOLECTADOS = {sumaFragmentos}
    MENOR VALOR FRAGMENTOS RECOLECTADOS = {menorFragmento}
    PROMEDIO TRUNCADO VALORES FRAGMENTOS RECOLECTADOS = {promedio}""")
        
        if puedeActivarCristal(fragmentosRecolectados, sumaFragmentos, menorFragmento, promedio):
            print("SI PUEDE ACTIVAR EL CRISTAL CÓSMICO")
            activaronCristal += 1
        else:
            print("NO PUEDE ACTIVAR EL CRISTAL CÓSMICO")
            noActivaronCristal += 1
        print("----------------------------------------------------------------")

        numeroCadete += 1
        totalCadetes += 1
    
    print("""REPORTE FINAL
=============""")
    if totalCadetes > 0:
        print(f"""TOTAL DE CADETES PROCESADOS : {totalCadetes}
% CADETES QUE ACTIVARON CRISTAL CÓSMICO = {round(calcularPorcentaje(activaronCristal,totalCadetes), 2)}
% CADETES QUE NO ACTIVARON CRISTAL CÓSMICO = {round(calcularPorcentaje(noActivaronCristal,totalCadetes), 2)}""")
    else:
        print("TOTAL DE CADETES PROCESADOS : 0")

main()
