#-----------------------------------------PROGRAMACIÓN I-----------------------------------------#
#-----------------------------------TRABAJO PRÁCTICO INTEGRADOR----------------------------------#
#-------------------ALUMNOS: Francisco Jesús Bultynch | Arnaiz Rodrigo Martín -------------------#

# Inicio del programa

#Declaración de funciones

# ---------- Lectura archivos csv ----------

def leer_csv(ARCHIVO):
    paises = []
    cont = 0
    with open(ARCHIVO, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector: # Se recorre el archivo por línea almacenando los datos de cada país en un diccionario
            cont += 1 #Cuenta las filas que se han ingresado
            poblacion = ingreso_cantidad_ok(fila['poblacion'].strip()) #Se valida que la población esté correctamente cargada en el archivo
            superficie = ingreso_cantidad_ok(fila['superficie'].strip()) #Se valida que la superficie esté correctamente cargada en el archivo
            if poblacion is None or superficie is None: #Si alguna de las funciones retorna None se saltea la carga de la fila
                print(f"\nLa superficie o población tienen valores incorrectos, se omitirá la carga de la fila nº {cont}.")
                input("\nPresione ENTER para continuar")
                continue  # salta la fila entera si alguno es inválido
            if not ingreso_nombre_ok(fila['nombre'].strip()) or not ingreso_nombre_ok(fila['continente'].strip()): #Si el continente o el país están vacíos se saltea la carga de la fila
                print(f"\nEl nombre o el continente están vacíos, se omitirá la carga de la fila nº {cont}.")
                input("\nPresione ENTER para continuar")                
                continue # salta la fila entera si alguno es inválido
            pais = {} # En cada bucle se resetea la variable del país
            pais['nombre'] = fila['nombre'].strip()
            pais['poblacion'] = int((fila['poblacion']).strip())
            pais['superficie'] = int((fila['superficie']).strip())
            pais['continente'] = fila['continente'].strip()
            paises.append(pais) # Se agrega el diccionario del país actual a la lista de países
        return paises

# ---------- Búsquedas ----------

def buscar_pais(paises, nombre):
    nombre = nombre.lower() 
    resultado = [] # inicializa la lista para almacenar resultados
    for p in paises: # Recorre la lista de países
        if nombre in p['nombre'].lower(): 
            resultado.append(p)
    return resultado


# ---------- Filtros ----------

def filtrar_por_continente(paises, continente):
    continente = continente.lower()
    filtrados = []
    for p in paises: # Recorre la lista de países
        if p['continente'].lower() == continente:
            filtrados.append(p)
    return filtrados


def filtrar_por_poblacion(paises, minimo, maximo):
    filtrados = []
    for p in paises:
        if p['poblacion'] >= minimo and p['poblacion'] <= maximo:
            filtrados.append(p) #Si el campo población está en el rango del mínimo y máximo se agrega la línea 
    return filtrados


def filtrar_por_superficie(paises, minimo, maximo):
    filtrados = []
    for p in paises:
        if p['superficie'] >= minimo and p['superficie'] <= maximo: 
            filtrados.append(p) #Si el campo superficie está en el rango del mínimo y máximo se agrega la línea 
    return filtrados


# ---------- Orden ----------

def obtener_nombre(pais): # Devuelve el nombre de cada país
    return pais['nombre']

def obtener_poblacion(pais):# Devuelve la poblacion de cada país
    return pais['poblacion']

def obtener_superficie(pais): # Devuelve la supuerficie de cada país
    return pais['superficie']

def ordenar_por_nombre(paises, descendente=False): #Devuelve la lista ordenada por el nombre 
    return sorted(paises, key=obtener_nombre, reverse=descendente) #Obtiene el parámetro de la función que llama y el orden por el booleano "descendente"

def ordenar_por_poblacion(paises, descendente=False): #Devuelve la lista ordenada por la población
    return sorted(paises, key=obtener_poblacion, reverse=descendente) #Obtiene el parámetro de la función que llama y el orden por el booleano "descendente"

def ordenar_por_superficie(paises, descendente=False): #Devuelve la lista ordenada por la superficie
    return sorted(paises, key=obtener_superficie, reverse=descendente) #Obtiene el parámetro de la función que llama y el orden por el booleano "descendente"


# ---------- Estadísticas ----------

def pais_mayor_poblacion(paises):
    mayor = paises[0] #Almacena al primer país de la lista como mayor
    for p in paises:
        if p['poblacion'] > mayor['poblacion']:
            mayor = p
    return mayor


def pais_menor_poblacion(paises):
    menor = paises[0] #Almacena al primer país de la lista como menor
    for p in paises:
        if p['poblacion'] < menor['poblacion']:
            menor = p
    return menor


def promedio_poblacion(paises):
    total = 0 #Inicializa el acumulador
    for p in paises:
        total += p['poblacion'] # Se acumula el contenido de todos los parámetros de población
    return total / len(paises)


def promedio_superficie(paises):
    total = 0 #Inicializa el acumulador
    for p in paises:
        total += p['superficie'] # Se acumula el contenido de todos los parámetros de superficie
    return total / len(paises)


def cantidad_por_continente(paises):
    conteo = {"África" : 0 , "América" : 0, "Asia" : 0, "Europa" : 0, "Oceanía" : 0} #Inicializa un diccionario para contar los países de cada continente
    #Se inicializa con los continentes en cero por si no hay países de un continente para que igualmente informe el nombre del continente en sí
    for p in paises:
        if p['continente'] in conteo: #Si el valor de continente del país coincide con uno del diccionario incrementa el valor en uno
            conteo[p['continente']] += 1
    return conteo


# ---------- Mostrar resultados ----------

def mostrar_paises(lista):
    if len(lista) == 0: # Si la lista está vacía se informa al usuario
        print('\nNo se encontraron resultados.')
        return

    for p in lista: #Si no se recorre la lista y se imprimen todos los resultados
        print(
            f"{p['nombre']:15} | Pob: {p['poblacion']:>10} | "f"Sup: {p['superficie']:>8} | {p['continente']}"
        )

# ------- Funciones de validación ---------

def control_existencia(nombre_archivo): # Función que controla la existencia del archivo .csv
    if not os.path.exists(nombre_archivo): #Si no se encuentra el archivo se informa al usuario 
        print(f"\nNo se pudo encontrar el archivo {nombre_archivo}, verificar el directorio del programa.")    
        return False
    return True

def ingreso_nombre_ok(nombre): #Verifica el que el ingreso de un nuevo título tenga sea válido (no vacío)
    if nombre == "":
        return False #Si el nombre ingresado está vacío retorna false
    return True

def estandarizar_continentes(continente): #Reemplaza el valor de los continentes ingresados sin tilde para coincidir con la base de datos
    match continente:
        case "africa":
            continente = "áfrica"
        case "america":
            continente = "américa"
        case "oceania":
            continente = "oceanía"
    return continente


def ingreso_cantidad_ok(cantidad):
    if not cantidad.isdigit(): #Si no es un entero positivo retorna None
        return None
    else:
        return int(cantidad) #Si es válido retorna el valor convertido de formato

def ingresar_sentido(): #Función que retorna el parámetro del orden
    print('\nA = Ascendente | D = Descendente')
    sentido = input('\nElija el sentido (Ascenedente/Descendente): ').upper().strip()

    if sentido == 'D': 
        return True # Se retorna True si se requiere orden descendente
    elif sentido == 'A':
        return False # Se retorna False si se requiere orden ascendente
    else:
        print(f"\n{sentido} no es válido, inténtelo nuevamente.")
        return None # Si el ingreso es otro se retorna None para el condicional

# ---------- Funciones de menú ------------


def mostrar_menu():
    print('\n---------- MENÚ PRINCIPAL ----------\n')
    print('1- Buscar país')
    print('2- Filtrar países')
    print('3- Ordenar países')
    print('4- Estadísticas')
    print('0- Salir')
    print('\n------------------------------------\n')


def menu_filtros(paises):
    opcion = ''
    while opcion != '0': #Se repite el bucle hasta que el usuario ingrese la opción de retornar
        print('\n---------- FILTROS ----------\n')
        print('1- Por continente')
        print('2- Por rango de población')
        print('3- Por rango de superficie')
        print('0- Volver')
        print('\n-------------------------------\n')

        opcion = input('Elija una opción: ')

        if opcion == '1':
            cont = input('\nIngrese continente: ').strip().lower()
            cont = estandarizar_continentes(cont) #Se llama a la función que acepta contientes sin tildes
            if ingreso_nombre_ok(cont): # Se llama a la función que verifica los ingresos vacíos
                resultado = filtrar_por_continente(paises, cont) #Se llama a la función que filtra por continentes y almacena en la lista de resultados
                mostrar_paises(resultado)
            else:
                print("\nEl valor no puede estar vacío. Inténtelo nuevamente.")
            input("\nPresione ENTER para continuar...")

        elif opcion == '2':
            minimo = input('\nPoblación mínima: ').strip()
            minimo = ingreso_cantidad_ok(minimo) # Se llama a la función que verifica que el ingreso sea un entero positivo
            if minimo != None:
                maximo = input('\nPoblación máxima: ').strip()
                maximo = ingreso_cantidad_ok(maximo) # Se llama a la función que verifica que el ingreso sea un entero positivo
                if maximo != None:
                    resultado = filtrar_por_poblacion(paises, minimo, maximo) #Se llama a la función que filtra por población y almacena en la lista de resultados
                    mostrar_paises(resultado)
                else:
                    print(f"\n{maximo} es un valor incorrecto, inténtelo nuevamente")
            else:
                print(f"\n{minimo} es un valor incorrecto, inténtelo nuevamente")
            input("\nPresione ENTER para continuar...")


        elif opcion == '3':
            minimo = input('\nSuperficie mínima: ').strip()
            minimo = ingreso_cantidad_ok(minimo) # Se llama a la función que verifica que el ingreso sea un entero positivo
            if minimo != None:
                maximo = input('\nSuperficie máxima: ').strip()
                maximo = ingreso_cantidad_ok(maximo) # Se llama a la función que verifica que el ingreso sea un entero positivo
                if maximo != None:
                    resultado = filtrar_por_superficie(paises, minimo, maximo) #Se llama a la función que filtra por superficie y almacena en la lista de resultados
                    mostrar_paises(resultado)
                else:
                        print(f"\n{maximo} es un valor incorrecto, inténtelo nuevamente")
            else:
                print(f"\n{minimo} es un valor incorrecto, inténtelo nuevamente")
            input("\nPresione ENTER para continuar...")

        elif opcion == '0':
            return
        
        else:
                print(f"{opcion} no es un valor válido. Inténtelo nuevamente.\n")
                input("\nPresione ENTER para continuar...")
        


def menu_ordenar(paises):
    opcion = ''
    while opcion != '0': #Se repite el bucle hasta que el usuario ingrese la opción de retornar
        print('\n---------- ORDENAMIENTOS ----------\n')
        print('1- Por nombre')
        print('2- Por población')
        print('3- Por superficie')
        print('0- Volver')
        print('\n-------------------------------------\n')

        opcion = input('Elija una opción: ').strip()

        if opcion == '1':
            descendente = ingresar_sentido() #Se llama a la función que informa el sentido seleccionado
            if descendente != None: #Si el ingreso no fue válido no se prosigue con el orden
                ordenados = ordenar_por_nombre(paises, descendente) #Se llama a la función que ordena por nombre del país y almacena en la lista de resultados
                mostrar_paises(ordenados)
            input("\nPresione ENTER para continuar...")

        elif opcion == '2':
            descendente = ingresar_sentido() #Se llama a la función que informa el sentido seleccionado
            if descendente != None: #Si el ingreso no fue válido no se prosigue con el orden
                ordenados = ordenar_por_poblacion(paises, descendente) #Se llama a la función que ordena por cantidad de población y almacena en la lista de resultados
                mostrar_paises(ordenados)
            input("\nPresione ENTER para continuar...")

        elif opcion == '3':
            descendente = ingresar_sentido() #Se llama a la función que informa el sentido seleccionado
            if descendente != None: #Si el ingreso no fue válido no se prosigue con el orden
                ordenados = ordenar_por_superficie(paises, descendente) #Se llama a la función que ordena por superficie y almacena en la lista de resultados
                mostrar_paises(ordenados)
            input("\nPresione ENTER para continuar...")
        
        elif opcion == '0':
            return
        
        else:
            print(f"\n{opcion} no es una opción válida. Inténtelo nuevamente.\n")
            input("\nPresione ENTER para continuar...")


def menu_estadisticas(paises):
    opcion = ''
    while opcion != '0': #Se repite el bucle hasta que el usuario ingrese la opción de retornar
        print('\n---------- ESTADÍSTICAS ----------\n')
        print('1- País con mayor población')
        print('2- País con menor población')
        print('3- Promedio de población')
        print('4- Promedio de superficie')
        print('5- Cantidad de países por continente')
        print('0- Volver')
        print('\n------------------------------------\n')

        opcion = input('Elija una opción: ').strip() 

        if opcion == '1':
            p = pais_mayor_poblacion(paises) # Se llama a la función que informa el país con mayor población
            mostrar_paises([p])
            input("\nPresione ENTER para continuar...")

        elif opcion == '2':
            p = pais_menor_poblacion(paises) # Se llama a la función que informa el país con menor población
            mostrar_paises([p])
            input("\nPresione ENTER para continuar...")

        elif opcion == '3':
            prom = promedio_poblacion(paises) # Se llama a la función que informa el promedio de población entre todos los países
            print(f'\nPromedio de población: {int(prom)} habitantes por país.') # Se redondea el promedio y se informa
            input("\nPresione ENTER para continuar...")

        elif opcion == '4':
            prom = promedio_superficie(paises) # Se llama a la función que informa el promedio de superficie entre todos los países
            print(f'\nPromedio de superficie: {int(prom)} km² por país.') # Se redondea el promedio y se informa
            input("\nPresione ENTER para continuar...")

        elif opcion == '5':
            conteo = cantidad_por_continente(paises) # Se llama a la función que retorna la cantidad de países de cada continente
            print('\nPaíses por continente:')
            for c in conteo: # Se recorre el diccionario y se muestran las claves (continentes) y valores (cantidad de países)
                print('- ', c, ':', conteo[c])
            input("\nPresione ENTER para continuar...")
        
        elif opcion == '0':
            return

        else:
            print(f"\n{opcion} no es un valor válido. Inténtelo nuevamente.")
            input("\nPresione ENTER para continuar...")


def main():
    ARCHIVO = 'paises.csv' #Se carga la ruta del archivo en una variable
    if control_existencia(ARCHIVO): #Se llama a la función que verifica la existencia del archivo de base de datos
        
        paises = leer_csv(ARCHIVO) #Se carga la base de datos en la lista de diccionarios

        opcion = ''

        while opcion != '0': #Se repite el bucle hasta que el usuario ingrese la opción de salir
            mostrar_menu() #Se llama a la función que muestra las opciones del menú principal 
            opcion = input('Elija una opción: ').strip()

            if opcion == '1':
                nombre = input('\nNombre del país a buscar: ').strip()
                if ingreso_nombre_ok(nombre): # Se llama a la función que verifica los ingresos vacíos
                    resultado = buscar_pais(paises, nombre) # Se llama a la función que retorna los datos de un país
                    mostrar_paises(resultado)
                else:         
                    print("\nEl valor no puede estar vacío. Inténtelo nuevamente.") # Se informa al usuario si se ingreso un nombre vacío
                input("\nPresione ENTER para continuar...")

            elif opcion == '2':
                menu_filtros(paises) # Se llama a la función que gestiona el submenú de filtros

            elif opcion == '3':
                menu_ordenar(paises) # Se llama a la función que gestiona el submenú de ordenamiento

            elif opcion == '4':
                menu_estadisticas(paises) # Se llama a la función que gestiona el submenú de informes
            
            elif opcion == '0': #Se sale del programa
                continue

            else:
                print(f"{opcion} no es un valor válido. Inténtelo nuevamente.\n")
                input("\nPresione ENTER para continuar...")
            
    return

# Programa Principal

# Importación de bibliotecas

import csv # Se importa para una mejor gestión de diccionarios en archivos csv
import os # Se importa para corroborar la existencia de la ruta del archivo

print("\n","-"*15,"Bienvenido al sistema de datos de países","-"*15,"\n")

main() #Se llama a la función del programa principal

print("\n","-"*15,"Gracias por usar el sistema","-"*15,"\n")