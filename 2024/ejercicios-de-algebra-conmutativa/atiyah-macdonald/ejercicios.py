# from crear_archivos import *
import os

tex_filename_extension = '.tex'

cap = 'ii'
carpeta_de_ejercicios = './cap-' + cap + '/'
carpeta_de_enunciados = './cap-' + cap + '/enunciados/'
carpeta_de_soluciones = './cap-' + cap + '/soluciones/'

base_ejercicio = carpeta_de_ejercicios + 'ejer'
base_enunciado = carpeta_de_enunciados + 'enun'
base_solucion = carpeta_de_soluciones + 'solu'

sobreescribir = False

fst = 1
lst = 29

lista = []
for n in range(fst, lst):
    z = len(str(lst)) - len(str(n))
    lista.append('0' * z + str(n))

### funciones para facilitar la creación de los archivos y directorios

def nuevo_archivo(nombre, contenido = '', sobreescribir = False):
    """
    si sobreescribir == False, verificar existencia de archivo nombre;
    crear nuevo archivo con nombre y contenido.
    """
    if( sobreescribir ):
        mode = 'w'
    else:
        mode = 'x'
    try:
        f = open(nombre, mode = mode)
    except FileExistsError as e:
        print(e)
    else:
        f.write(contenido)
        f.close()

def path_to_nuevo_archivo_numerado(base, n, filename_extension):
    """ n : nombre (str) o número (int o tipo numérico) de archivo """
    return ( base + str(n) + filename_extension )

def nuevo_archivo_numerado(base, n, filename_extension, contenido = '', \
        sobreescribir = False):
    """
    n : nombre (str) o número (int o tipo numérico) de archivo;
    crea nuevo archivo (si no existe) y devuelve su ubicación
    """
    path_to_file = path_to_nuevo_archivo_numerado(base, n, filename_extension)
    nuevo_archivo(path_to_file, contenido, sobreescribir)
    return path_to_file

def es_directorio_valido(nueva_carpeta):
    """
    True, si len(nueva_carpeta) > 0 y si el nombre nueva_carpeta no está en uso
    """
    return ( ( len( nueva_carpeta ) > 0 ) and \
            ( not os.path.exists(nueva_carpeta) ) )

### funciones para crear los archivos ejer*, enun* y solu*

def crear_enunciado_numerado(n, sobreescribir):
    """
    enunciado del ejercicio n;
    verificar la existencia de archivo;
    si sobreescribir == True, crear un nuevo archivo vacío.
    """
    contenido = ''
    return nuevo_archivo_numerado(base_enunciado, n, tex_filename_extension, \
            contenido, sobreescribir)

def crear_solucion_numerada(n, sobreesribir):
    """
    solución del ejercicio n;
    verificar la existencia de archivo;
    si sobreescribir == True, crear un nuevo archivo vacío.
    """
    contenido = ''
    return nuevo_archivo_numerado(base_solucion, n, tex_filename_extension, \
            contenido, sobreescribir)

def crear_ejercicio_numerado(n, path_to_enunciado, path_to_solucion, \
        sobreescribir):
    """crear archivo genérico para el ejercicio n"""
    contenido = '\\bej' + cap + '\n' + \
            '\t\\label{ejer:cap' + cap + ':' + str(n) + '}\n' + \
            '\t\\input{' + path_to_enunciado + '}\n' + \
            '\\fej' + cap + '\n' + \
            '\\begin{solucion}\n' + \
            '\t\\input{' + path_to_solucion + '}\n' + \
            '\\end{solucion}'
    return nuevo_archivo_numerado(base_ejercicio, n, tex_filename_extension, \
            contenido, sobreescribir)

def crear_cap():
    nombre = carpeta_de_ejercicios + 'cap-' + cap + tex_filename_extension
    contenido = '\\theoremstyle{definition}\n' + \
                '\\newtheorem{ejercap' + cap + '}{Ejercicio}[section]\n\n' + \
                '\\newcommand{\bej' + cap + '}{\\begin{ejercap' + cap + '}}\n' + \
                '\\newcommand{\fej' + cap + '}{\\end{ejercap' + cap + '}}\n'
    nuevo_archivo(nombre, contenido)
    return None

### functions for creating and populating folders

def crear_carpetas_de_ejercicios(carpeta_de_ejercicios, \
        carpeta_de_enunciados, carpeta_de_soluciones):
    """
    crear los directorios necesarios para una lista de ejercicios.
    """
    if es_directorio_valido(carpeta_de_ejercicios):
        os.mkdir(carpeta_de_ejercicios)
    if es_directorio_valido(carpeta_de_enunciados):
        os.mkdir(carpeta_de_enunciados)
    if es_directorio_valido(carpeta_de_soluciones):
        os.mkdir(carpeta_de_soluciones)

def actualizar_directorio_de_ejercicios(lista, sobreescribir):
    """
    lista : lista de ejercicios (lista de str, lista de ints, range, ...)
    verificar la existencia de los archivos de ejercicios, en caso de no
    existir crear nuevos.
    """
    for n in lista:
        path_to_enunciado = crear_enunciado_numerado(n, sobreescribir)
        path_to_solucion = crear_solucion_numerada(n, sobreescribir)
        crear_ejercicio_numerado(n, path_to_enunciado, path_to_solucion, \
                sobreescribir)

###

crear_carpetas_de_ejercicios(carpeta_de_ejercicios, carpeta_de_enunciados, \
        carpeta_de_soluciones)

actualizar_directorio_de_ejercicios(lista, sobreescribir)

crear_cap()
