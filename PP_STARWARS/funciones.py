import re
import json

def cargar_json(path:str):
    with open (path,"r") as archivo:
        data = json.load(archivo)
    return data["results"]

def importar_csv(destino:str,lista:list):
    with open(destino,"w") as archivo:
        for personaje in lista:
            archivo.write("Nombre: {0} | Genero: {1}\n".format(personaje["name"],personaje["gender"]))


def ordenar_personajes(lista:list,key:str)->list:
    '''
    ordena una lista de mayor a menor segun la key ingresada

    lista: lista a usar
    key: key ingresada para comparar

    devuelve la lista ordenada
    '''
    lista_a_ordenar = lista.copy()
    swap_flag = True
    limite = 1

    while swap_flag == True:
        swap_flag = False
        for i in range(len(lista_a_ordenar) - limite):
            if int(lista_a_ordenar[i][key]) > int(lista_a_ordenar[i+1][key]):
                lista_a_ordenar[i],lista_a_ordenar[i+1] = lista_a_ordenar[i+1],lista_a_ordenar[i]
                swap_flag = True
        limite += 1
    return lista_a_ordenar


def listar_personajes(lista:list,key:str)->str:
    '''
    itera e imprime todos los personajes de una lista

    lista: lista a usar
    key: key ingresada para mostrar

    devuelve la lista de los personajes
    '''
    lista_a_ordenar = lista.copy()
    if lista_a_ordenar:
        for personaje in lista_a_ordenar:
            print("Nombre: {0} | Genero: {1} | {2}: {3}\n".format(personaje["name"],personaje["gender"],key,personaje[key]))

def mostrar_mas_alto(lista:list,genero:str)->str:
    '''
    itera y compara por altura los personajes de una lista

    lista: lista a usar
    genero: genero que se usa para comparar

    devuelve uns str con el mas alto
    '''
    if lista:
        max = lista[0]
        for personaje in lista:
            if personaje["gender"] == "male" and genero == "male":
                if int(personaje["height"]) > int(max["height"]):
                    max = personaje
            elif personaje["gender"] == "female" and genero == "female":
                if int(personaje["height"]) > int(max["height"]):
                    max = personaje
            elif personaje["gender"] == "n/a" and genero == "n/a":
                if int(personaje["height"]) > int(max["height"]):
                    max = personaje
        print("Nombre: {0} | Altura: {1}\n".format(max["name"],max["height"]))

def mostrar_alto(lista:list,genero:str)->str:
    '''
    itera y compara por altura los personajes de una lista

    lista: lista a usar
    genero: genero que se usa para comparar

    devuelve uns str con el mas alto
    ''' 

    if lista:
        lista_nueva = []
        for personaje in lista:
            if genero in personaje["gender"]:
                lista_nueva.append(personaje)
            
        max = lista_nueva[0]
        for personaje in lista_nueva:
            if int(personaje["height"]) > int(max["height"]):
                max = personaje
        print("Nombre: {0} | Altura: {1}\n".format(max["name"],max["height"]))


def buscar_personajes(lista:list,busqueda:str)->str:
    '''
    busca el nombre que coincide con el str ingresado

    lista: lista a usar
    busqueda: pedazo de str a encontrar en el nombre

    devuelve un str con el nombre y genero
    '''

    for personaje in lista:
        if re.match(busqueda,personaje["name"],re.IGNORECASE):
            print("Nombre: {0} | Genero: {1}\n".format(personaje["name"],personaje["gender"]))