def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def experiencia(n):
    suma = 0
    for k in range(n):
        numerador = (2 * k) ** (2 * k + 1)
        denominador = factorial(k + 1)
        suma += numerador / denominador
    return int(suma ** 0.5)               
    

def espiritu(n):
    sumaDiv = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 1:
            sumaDiv += i
    return sumaDiv


def chakra(m,n):
    numero = m * n
    sumaDigitosPares = 0
    while numero > 0:
        ultDigito = numero % 10
        if ultDigito % 2 == 0:
            sumaDigitosPares += ultDigito
        numero //= 10
    return sumaDigitosPares


def contieneAl2(n):
    while n > 0:
        ultDigito = n % 10
        if ultDigito == 2:
            return True
        n //= 10
    return False


def calcularPorcentaje(parcial,total):
    if total == 0:
        return 0.0
    return (parcial/total) * 100


def main():
    totalNinjas = 0
    contadorPromovidos = 0
    sumaIvs = 0
    while True:
        nombre = input()
        if nombre == "FIN":
            break

        mce = int(input())
        vsm = int(input())
        aef = int(input())
        nci = int(input())

        ivs = (experiencia(mce) + espiritu(vsm)) * chakra(aef,nci)
        sumaIvs += ivs
        

        print(f"Ninja {nombre}")
        print(f"Índice de Voluntad Shinobi = {ivs}")

        if ivs > 5000 and contieneAl2(ivs):
            print("*** PROMOVIDO A JERARQUÍA CHUNIN ***")
            contadorPromovidos += 1
        print()
        totalNinjas += 1
        
    print(f"""REPORTE FINAL
============
Total de ninjas procesados = {totalNinjas}""")

    if totalNinjas > 0:
        promedio = int(sumaIvs / totalNinjas)
        print()
        print(f"""Promedio IVS ninjas procesados = {promedio}
{round(calcularPorcentaje(contadorPromovidos,totalNinjas) , 1)}% de los ninjas fueron promovidos a la jerarquía chünin""")
        

main()