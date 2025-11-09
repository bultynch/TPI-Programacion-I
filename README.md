# Trabajo Práctico Integrador – Programación 1

Integrantes:
Arnaiz Rodrigo Martín - arnaizrodrigomartin@gmail.com
Bultynch Francisco Jesús - bultynch98@gmail.com

##  Descripción del programa

Este programa permite gestionar un conjunto de datos sobre países utilizando: listas, diccionarios, funciones, estructuras condicionales y repetitivas.  

El sistema carga la información desde un archivo CSV, permite realizar búsquedas, filtros, ordenamientos y genera diversas estadísticas a partir del dataset.

El objetivo del proyecto es aplicar las bases de la programación estructurada, modularizar correctamente las funciones y trabajar con archivos externos.


### Funcionalidades principales

#### Búsqueda
- Buscar países por nombre (coincidencia parcial o exacta).

#### Filtros
- Filtrar países por continente.
- Filtrar por rango de población.  
- Filtrar por rango de superficie.

#### Ordenamientos
- Ordenar por nombre (ascendete/descendente).  
- Ordenar por población (ascendente/descendente).  
- Ordenar por superficie (ascendente/descendente).  

#### Estadísticas
- País con mayor y menor población.   
- Promedio de población.  
- Promedio de superficie.  
- Cantidad de países por continente.  

#### Dataset

El archivo paises.csv contiene los siguientes campos:

- 'nombre'
- 'poblacion'
- 'superficie'
- 'continente'

Con los siguientes ejemplos:

Argentina,45500000,2780400,América
Brasil,214000000,8515767,América
Japón,125800000,377975,Asia
Alemania,83150000,357022,Europa
Egipto,110000000,1010408,África
Australia,25690000,7700000,Oceanía

-------------

## Instrucciones de uso

1. Contar con Pyhton 3.x instalado.
2. Descargar todos los archivos del repositorio.
3. Ejecutar en la consola.
4. Navegar por el menú utlizando los números para seleccionar las opciones.

----------

## Ejemplos de entrada y salida.

#---------- MENÚ PRINCIPAL ----------
1- Buscar país
2- Filtrar países
3- Ordenar países
4- Estadísticas
0- Salir
#------------------------------------

--- Ejemplo 1 ---

- Entrada: 1
- Salida: Nombre del país a buscar:
- Entrada: argentina
- Salida: Argentina       | Pob:   45500000 | Sup:  2780400 | América

--- Ejemplo 2 ---

- Entrada: 4
- Salida: ---------- ESTADÍSTICAS ----------
1- País con mayor población
2- País con menor población
3- Promedio de población
4- Promedio de superficie
5- Cantidad de países por continente
0- Volver
------------------------------------
- Entrada: 1
- Salida: Brasil          | Pob:  214000000 | Sup:  8515767 | América

--- Ejemplo 3 ---

- Entrada: 0
- Salida: Programa finalizado.

## Participacion de los integrantes

Ambos integrantes participaron en:
- Diseño del programa.
- Elaboración de funciones.
- Pruebas y depuración.
- Grabación del video explicativo.