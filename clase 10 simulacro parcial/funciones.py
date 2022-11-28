import re
import json
from unittest.util import strclass

def cargar_archivo(nombre_archivo:str)->str:
    '''
    carga el archivo json

    primer parametro: direccion del archivo
    segundo parametro: r o w segun corresponda

    '''
    with open (nombre_archivo,"r") as archivo:
        resultado = json.load(archivo)
        resultado_lista = resultado["heroes"]
        return resultado_lista


def validar_dato(respuesta:str,regex:str):
    '''
    Valida uno o mas numeros

    respuesta: texto a validar
    regex : regex de busqueda 
    '''
    if respuesta:
        if re.search(regex,respuesta):
            retorno = respuesta
        else:
            retorno = -1
    else:
        retorno = -1
    return retorno

def validar_len_lista(lista:list,numero:int)->int:
    if len(lista) > 0 and len(lista) > numero:
        return numero
    else:
        print("El numero supera el tamaño de la lista")
        return -1

def listar_heroes(lista:list,key:str)->str:
    '''
    imprime la lista de heroes dejando como maximo el numero que se pide

    1er parametro: lista a usar
    2do: numero maximo
    3ro: key que se quiere mostrar
    devuelve error si la lista es -1 
    '''
    if lista == -1:
        print("Error!")
    else:
        for heroe in lista:
            print("Nombre: {0} | Identidad: {1} | {2}: {3}".format(heroe["nombre"],heroe["identidad"],key.capitalize(),heroe[key]))

# def listar_heroes_maximos(lista:list,key:str)->str:
#     numero = input("Ingrese un numero")
#     numero = int(numero)
#     listar_heroes(lista,numero,key)

def buscar_max_min(lista:list,clave:str,tipo:str)->list:
    '''
    calcula el asc o desc de una lista

    lista: lista a usar
    clave: key a comparar
    tipo: asc o desc

    retorna el diccionario asc o desc segun el clave
    devuelve -1 si el tipo es -1 
    '''
    if tipo == -1:
        retorno = -1
    else:
        if len(lista) > 0:
            elemento_max_min = 0 #0 para agarrar la posicion 0
            for elemento in range(len(lista)):
                if tipo == "asc" and (lista[elemento][clave] > lista[elemento_max_min][clave]):
                    elemento_max_min = elemento
                elif tipo == "desc" and (lista[elemento][clave] < lista[elemento_max_min][clave]):
                    elemento_max_min = elemento
            retorno = elemento_max_min
    return retorno

def ordenar_lista(lista:list,clave:str,tipo:str)->list:
    '''
    ordena una lista
    
    lista: lista a usar
    valor: key a comparar
    tipo: asc o desc
    
    retorna una copia de la lista ordenada
    devuelve -1 si el tipo es -1 
    '''
    if tipo == -1:
        retorno = -1
    else:  
        lista_a_ordenar = lista.copy() # lista[:]
        lista_ordenada = []
        while(len(lista_a_ordenar)>0):
            index_min_max = buscar_max_min(lista_a_ordenar,clave,tipo)
            elemento = lista_a_ordenar.pop(index_min_max)
            lista_ordenada.append(elemento)
            retorno = lista_ordenada
    return retorno


def calcular_promedio_key(lista:list,key:str)->int:

    '''
    calcula el promedio de enteros en una key

    lista: lista  a usar
    key : key a acumular
    devuelve -1 si la key es -1 
    '''
    if key == -1:
        retorno = -1
    else:
        acumulador_de_key = 0
        contador = 0
        if lista:
            for heroe in lista:
                acumulador_de_key += heroe[key]
                contador += 1
            promedio = acumulador_de_key / contador
            retorno = promedio
    return retorno
        
def comparar_con_promedio(lista:list,promedio:int,key:str,tipo:str)->list:
    '''
    compara la key ingresada con un promedio de la misma
    agrega a una lista segun se elija mayor o menor

    lista: lista a usar
    promedio: numero a comparar con las keys numericas
    key: clave a ser comparada
    tipo: mayor o menor segun quiera el usuario

    devuelve la lista obtenida segun el tipo requerido
    devuelve -1 si el tipo es -1 
    '''
    if tipo == -1:
        retorno = -1
    else:   
        lista_a_ordenar = lista.copy() # lista[:]
        lista_ordenada = []
        if lista_a_ordenar:
            for heroe in lista_a_ordenar:
                if tipo == "mayor" and promedio < heroe[key]:
                    lista_ordenada.append(heroe)
                if tipo == "menor" and promedio > heroe[key]:
                    lista_ordenada.append(heroe)
            retorno =  lista_ordenada
    return retorno

def buscar_por_inteligencia(lista:list,tipo:str)->list:
    '''
    filtra una lista segun el tipo de inteligencia que se busque

    lista: lista a usar
    tipo: good | average | high segun se quiera usar

    devuelve una lista con los diccionarios de los heroes con ese tipo de inteligencia
    devuelve -1 si el tipo es -1
    '''

    if tipo == -1:
        retorno = -1
    else:
        lista_a_ordenar = lista.copy() # lista[:]
        lista_ordenada = []
        if lista_a_ordenar:
            for heroe in lista_a_ordenar:
                if tipo in heroe["inteligencia"]:
                    lista_ordenada.append(heroe)
            retorno = lista_ordenada
    return retorno

def exportar_csv(lista:list,ubicacion:str,key:str):
    '''
    guarda una lista en un archivo csv

    lista: lsta a guardar
    ubicacion: donde guardarlo
    key: clave usada para mostrar los datos
    
    '''
    with open(ubicacion,"w") as archivo:
        for heroe in lista:
            archivo.write("Nombre: {0} | Identidad: {1} | {2}: {3}\n".format(heroe["nombre"],heroe["identidad"],key.capitalize(),heroe[key]))