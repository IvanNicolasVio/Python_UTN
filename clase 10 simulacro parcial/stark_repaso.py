import funciones as func

INPUT = "C:/Users/Iván/Desktop/Python_UTN/clase 10 simulacro parcial/data_stark.json"
OUTPUT = "C:/Users/Iván/Desktop/Python_UTN/clase 10 simulacro parcial/data_stark.csv"


def imprimir_menu()->str:
    lista_de_heroes = func.cargar_archivo(INPUT)
    while True:
        print(  "\n"
                "1-Listar un numero de heroes\n"
                "2-Ordenar y listar heroes por altura\n"
                "3-Ordenar y listar heroes por fuerza\n"
                "4-Calcular promedio y filtrar\n"
                "5-Listar por inteligencia\n"
                "6-Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente\n"
                "7-Salir\n")
        respuesta = input("\n\n Ingrese un numero >>> ")
        respuesta = func.validar_dato(respuesta,"^[1-7]{1}$")


        if respuesta == "1":   
            key = "fuerza"   
            respuesta = input("Numero de heroes a imprimir > ")
            respuesta = int(func.validar_dato(respuesta,"^[0-9]{1,4}$"))
            respuesta = func.validar_len_lista(lista_de_heroes,respuesta)
            lista_ordenada = lista_de_heroes[:respuesta].copy()
            func.listar_heroes(lista_ordenada,key)
        elif respuesta == "2":
            key = "altura"
            respuesta = input("Como quiere ordenar la lista? (asc/desc) > ")
            respuesta = func.validar_dato(respuesta,"^asc|desc$")
            lista_ordenada = func.ordenar_lista(lista_de_heroes,key,respuesta)
            func.listar_heroes(lista_ordenada,key)
        elif respuesta == "3":
            key = "fuerza"
            respuesta = input("Como quiere ordenar la lista? (asc/desc) > ")
            respuesta = func.validar_dato(respuesta,"^asc|desc$")
            lista_ordenada = func.ordenar_lista(lista_de_heroes,key,respuesta)
            func.listar_heroes(lista_ordenada,key)
        elif respuesta == "4":
            key = input("Que dato quiere comparar? altura/peso/fuerza > ")
            key = func.validar_dato(key,"^altura|peso|fuerza$")
            tipo = input("Como lo quiere comparar? mayor|menor > ")
            tipo = func.validar_dato(tipo,"^mayor|menor$")
            promedio = func.calcular_promedio_key(lista_de_heroes,key)
            print("El promedio es {0} \n".format(promedio))
            lista_ordenada = func.comparar_con_promedio(lista_de_heroes,promedio,key,tipo)
            func.listar_heroes(lista_ordenada,key)
        elif respuesta == "5":
            key = "inteligencia"
            tipo = input("Que dato quiere listar? good|average|high > ")
            tipo = func.validar_dato(tipo,"^good|average|high$")
            lista_ordenada = func.buscar_por_inteligencia(lista_de_heroes,tipo)
            func.listar_heroes(lista_ordenada,key)
        elif respuesta == "6":
            func.exportar_csv(lista_ordenada,OUTPUT,key)
            print("Lista guardada con exito!")
        elif respuesta == "7":
            print("Nos vemos!")
            break
        else:
            print("Numero incorrecto")

imprimir_menu()