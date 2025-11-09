from funciones import (
    leer_csv,
    buscar_pais,
    filtrar_por_continente,
    filtrar_por_poblacion,
    filtrar_por_superficie,
    ordenar_por_nombre,
    ordenar_por_poblacion,
    ordenar_por_superficie,
    pais_mayor_poblacion,
    pais_menor_poblacion,
    promedio_poblacion,
    promedio_superficie,
    cantidad_por_continente,
    mostrar_paises
)


def mostrar_menu():
    print('\n---------- MENÚ PRINCIPAL ----------')
    print('1- Buscar país')
    print('2- Filtrar países')
    print('3- Ordenar países')
    print('4- Estadísticas')
    print('0- Salir')
    print('------------------------------------\n')


def menu_filtros(paises):
    print('\n---------- FILTROS ----------')
    print('1- Por continente')
    print('2- Por rango de población')
    print('3- Por rango de superficie')
    print('0- Volver')
    print('-------------------------------\n')

    opcion = input('Elija una opción: ')

    if opcion == '1':
        cont = input('Ingrese continente: ')
        resultado = filtrar_por_continente(paises, cont)
        mostrar_paises(resultado)

    elif opcion == '2':
        minimo = int(input('Población mínima: '))
        maximo = int(input('Población máxima: '))
        resultado = filtrar_por_poblacion(paises, minimo, maximo)
        mostrar_paises(resultado)

    elif opcion == '3':
        minimo = int(input('Superficie mínima: '))
        maximo = int(input('Superficie máxima: '))
        resultado = filtrar_por_superficie(paises, minimo, maximo)
        mostrar_paises(resultado)


def menu_ordenar(paises):
    print('\n---------- ORDENAMIENTOS ----------')
    print('1- Por nombre')
    print('2- Por población')
    print('3- Por superficie')
    print('0- Volver')
    print('-------------------------------------\n')

    opcion = input('Elija una opción: ')

    print('\nA = Ascendente | D = Descendente')
    sentido = input('Elija el sentido (Ascenedente/Descendente): ').upper()

    if sentido == 'D':
        descendente = True
    else:
        descendente = False

    if opcion == '1':
        ordenados = ordenar_por_nombre(paises, descendente)
        mostrar_paises(ordenados)

    elif opcion == '2':
        ordenados = ordenar_por_poblacion(paises, descendente)
        mostrar_paises(ordenados)

    elif opcion == '3':
        ordenados = ordenar_por_superficie(paises, descendente)
        mostrar_paises(ordenados)


def menu_estadisticas(paises):
    print('\n---------- ESTADÍSTICAS ----------')
    print('1- País con mayor población')
    print('2- País con menor población')
    print('3- Promedio de población')
    print('4- Promedio de superficie')
    print('5- Cantidad de países por continente')
    print('0- Volver\n')
    print('------------------------------------\n')

    opcion = input('Elija una opción: ')

    if opcion == '1':
        p = pais_mayor_poblacion(paises)
        mostrar_paises([p])

    elif opcion == '2':
        p = pais_menor_poblacion(paises)
        mostrar_paises([p])

    elif opcion == '3':
        prom = promedio_poblacion(paises)
        print('Promedio de población:', int(prom))

    elif opcion == '4':
        prom = promedio_superficie(paises)
        print('Promedio de superficie:', int(prom))

    elif opcion == '5':
        conteo = cantidad_por_continente(paises)
        print('\nPaíses por continente:')
        for c in conteo:
            print('- ', c, ':', conteo[c])


def main():
    ARCHIVO = 'paises.csv'
    paises = leer_csv(ARCHIVO)

    opcion = ''

    while opcion != '0':
        mostrar_menu()
        opcion = input('Elija una opción: ')

        if opcion == '1':
            nombre = input('Nombre del país a buscar: ')
            resultado = buscar_pais(paises, nombre)
            mostrar_paises(resultado)

        elif opcion == '2':
            menu_filtros(paises)

        elif opcion == '3':
            menu_ordenar(paises)

        elif opcion == '4':
            menu_estadisticas(paises)

    print('\nPrograma finalizado.')


main()
