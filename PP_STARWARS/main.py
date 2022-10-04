'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones
FILE = "C:/Users/Iván/Desktop/Python_UTN/Star/PP_STARWARS/PP_STARWARS/data.json"
OUTPUT = "C:/Users/Iván/Desktop/Python_UTN/Star/PP_STARWARS/PP_STARWARS/starwars.csv"
def starwars_app():
    lista_personajes = funciones.cargar_json(FILE)
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            personajes_ordenados = funciones.ordenar_personajes(lista_personajes,"height")
            funciones.listar_personajes(personajes_ordenados,"height")
        elif(respuesta=="2"):
            funciones.mostrar_alto(lista_personajes,"male")
            funciones.mostrar_alto(lista_personajes,"female")
            funciones.mostrar_alto(lista_personajes,"n/a")
        elif(respuesta=="3"):
            personajes_ordenados = funciones.ordenar_personajes(lista_personajes,"mass")
            funciones.listar_personajes(personajes_ordenados,"mass")
        elif(respuesta=="4"):
            busqueda = input("Ingrese un nombre > ")
            funciones.buscar_personajes(lista_personajes,busqueda)
        elif(respuesta=="5"):
            funciones.importar_csv(OUTPUT,personajes_ordenados)
            print("Lista guardada con exito")
        elif(respuesta=="6"):
            print("Adios Maestro")
            break


starwars_app()

