from data_stark import lista_personajes
import re

def validar_un_numero(respuesta:str):
    '''
    Valida uno o mas numeros

    respuesta: texto a validar
    '''
    while True:
        if re.search("^[0-6]{1}$",respuesta) == None:
            respuesta = input("Ingrese un numero correcto >>> ")
        else:
            break
    return respuesta
    

def imprimir_menu()->str:
    while True:
        print(  "1-Primera opcion\n"
                "2-Segunda opcion\n"
                "3-Tercera opcion\n"
                "4-Cuarta opcion\n"
                "5-Quinta opcion\n"
                "6-Salir\n")
        respuesta = input("\n\n Ingrese un numero >>> ")

        validar_un_numero(respuesta)

        if respuesta == "1":
            print("Primera opcion")
        elif respuesta == "2":
            print("Segunda opcion")
        elif respuesta == "3":
            print("Tercera opcion")
        elif respuesta == "4":
            print("Cuarta opcion")
        elif respuesta == "5":
            print("Quinta opcion")
        elif respuesta == "6":
            print("Nos vemos!")
            break


def validar_string(texto:str,tipo:str="entero"):
    '''
    valida un entero o un string

    texto : string a analizar
    tipo : string/entero/flotante

    retorna el texto validado
    '''
    while True:
        if re.search("^[0-9]+$",texto) == None and tipo == "entero":
            texto = input("Ingrese un numero >>> ")
        elif re.search("^[0-9.]+$",texto) == None and tipo == "flotante":
            texto = input("Ingrese un numero >>> ")
        elif re.search("^[a-zA-Z]+$",texto) == None and tipo == "string":
            texto = input("Ingrese solo letras > ")
        else:
            break
    return texto

def calcular_max_min(lista:list,clave:str,tipo:str="maximo")->dict:
    '''
    calcula el maximo o minimo de una lista

    lista: lista a usar
    clave: key a comparar
    tipo: maximo o minimo

    retorna el diccionario maximo o minimo segun el clave
    '''
    numero_max_min = lista[0]
    for elemento in lista:
        if ((float(elemento[clave]) > float(numero_max_min[clave])) and tipo == "maximo"):
            numero_max_min = elemento
        elif ((float(elemento[clave]) < float(numero_max_min[clave])) and tipo == "minimo"):
            numero_max_min = elemento
    return numero_max_min

def buscar_max_min(lista:list,clave:str,tipo:str="maximo")->list:
    '''
    calcula el maximo o minimo de una lista

    lista: lista a usar
    clave: key a comparar
    tipo: maximo o minimo

    retorna el diccionario maximo o minimo segun el clave
    '''
    
    if len(lista) > 0:
        elemento_max_min = 0 #0 para agarrar la posicion 0
        for elemento in range(len(lista)):
            if tipo == "maximo" and (lista[elemento][clave] > lista[elemento_max_min][clave]):
                elemento_max_min = elemento
            elif tipo == "minimo" and (lista[elemento][clave] < lista[elemento_max_min][clave]):
                elemento_max_min = elemento
    return elemento_max_min

        
def ordenar_lista(lista:list,clave:str,tipo:str="maximo")->list:
    '''
    ordena una lista
    
    lista: lista a usar
    valor: key a comparar
    tipo: maximo o minimo
    
    retorna una copia de la lista ordenada
    '''
    
    lista_a_ordenar = lista.copy() # lista[:]
    lista_ordenada = []
    while(len(lista_a_ordenar)>0):
        index_min_max = buscar_max_min(lista_a_ordenar,clave,tipo)
        elemento = lista_a_ordenar.pop(index_min_max)
        lista_ordenada.append(elemento)
    return lista_ordenada

def imprimir_datos(lista:list):
    for elemento in lista:
        print("Nombre:{0} | altura:{1} | Fuerza:{2}".format(elemento["nombre"],elemento["altura"],elemento["fuerza"]))

def sanitizar_flotante(lista:list,clave:str):
    for elemento in lista:
        elemento[clave] = float(elemento[clave])
    return lista

def sanitizar_entero(lista:list,clave:str):
    for elemento in lista:
        elemento[clave] = int(elemento[clave])
    return lista



sanitizar_flotante(lista_personajes,"altura")
imprimir_datos(ordenar_lista(lista_personajes,"altura","maximo"))

#print(calcular_max_min(lista_personajes,"peso","maximo"))