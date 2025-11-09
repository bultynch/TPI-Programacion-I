import csv

# ---------- Lectura archivos csv ----------

def leer_csv(ARCHIVO):
    paises = []

    archivo = open(ARCHIVO, encoding='utf-8')
    lector = csv.DictReader(archivo)

    for fila in lector:
        pais = {}
        pais['nombre'] = fila['nombre']
        pais['poblacion'] = int(fila['poblacion'])
        pais['superficie'] = int(fila['superficie'])
        pais['continente'] = fila['continente']
        paises.append(pais)

    archivo.close()
    return paises


# ---------- Búsquedas ----------

def buscar_pais(paises, nombre):
    nombre = nombre.lower()
    resultado = []
    for p in paises:
        if nombre in p['nombre'].lower():
            resultado.append(p)
    return resultado


# ---------- Filtros ----------

def filtrar_por_continente(paises, continente):
    continente = continente.lower()
    filtrados = []
    for p in paises:
        if p['continente'].lower() == continente:
            filtrados.append(p)
    return filtrados


def filtrar_por_poblacion(paises, minimo, maximo):
    filtrados = []
    for p in paises:
        if p['poblacion'] >= minimo and p['poblacion'] <= maximo:
            filtrados.append(p)
    return filtrados


def filtrar_por_superficie(paises, minimo, maximo):
    filtrados = []
    for p in paises:
        if p['superficie'] >= minimo and p['superficie'] <= maximo:
            filtrados.append(p)
    return filtrados


# ---------- Orden ----------

def obtener_nombre(pais):
    return pais['nombre']

def obtener_poblacion(pais):
    return pais['poblacion']

def obtener_superficie(pais):
    return pais['superficie']


def ordenar_por_nombre(paises, descendente=False):
    return sorted(paises, key=obtener_nombre, reverse=descendente)

def ordenar_por_poblacion(paises, descendente=False):
    return sorted(paises, key=obtener_poblacion, reverse=descendente)

def ordenar_por_superficie(paises, descendente=False):
    return sorted(paises, key=obtener_superficie, reverse=descendente)


# ---------- Estadísticas ----------

def pais_mayor_poblacion(paises):
    mayor = paises[0]
    for p in paises:
        if p['poblacion'] > mayor['poblacion']:
            mayor = p
    return mayor


def pais_menor_poblacion(paises):
    menor = paises[0]
    for p in paises:
        if p['poblacion'] < menor['poblacion']:
            menor = p
    return menor


def promedio_poblacion(paises):
    total = 0
    for p in paises:
        total += p['poblacion']
    return total / len(paises)


def promedio_superficie(paises):
    total = 0
    for p in paises:
        total += p['superficie']
    return total / len(paises)


def cantidad_por_continente(paises):
    conteo = {}
    for p in paises:
        cont = p['continente']
        if cont in conteo:
            conteo[cont] += 1
        else:
            conteo[cont] = 1
    return conteo


# ---------- Mostrar resultados ----------

def mostrar_paises(lista):
    if len(lista) == 0:
        print('No se encontraron resultados.')
        return

    for p in lista:
        print(
            f"{p['nombre']:15} | Pob: {p['poblacion']:>10} | "f"Sup: {p['superficie']:>8} | {p['continente']}"
        )

