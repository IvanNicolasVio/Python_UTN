'''
La división de alimentos de industrias Wayne está trabajando en un pequeño software para cargar datos de heroínas y héroes, 
para para tener un control de las condiciones de heroes existentes, nos solicitan:
Nombre de Heroína/Héroe
EDAD (mayores a 18 años)
Sexo ("m", "f" o "nb")
Habilidad ("fuerza", "magia", "inteligencia").
A su vez, el programa deberá mostrar por consola lo siguiente:
Dar el nombre de Héroe | Heroína de 'fuerza' más joven.A
El sexo y nombre de Heroe | Heroína de mayor edad. B 
La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'. C
El promedio de edad entre Heroinas. D
El promedio de edad entre Heroes de fuerza. E

Vio Ivan Nicolas
'''

respuesta = "si"
bandera_mas_joven = True
bandera_mas_viejo = True
edad_total_heroe_fuerza = 0
edad_total_heroina = 0
contador_de_heroinas = 0
contador_de_heroinas_con_habilidades = 0
contador_heroes_fuerza = 0


while respuesta == "si":
    nombre = input("Ingrese el nombre ")

    while True:
        edad = int(input("Ingrese la edad "))
        if edad > 17:
            break
    
    while True:
        sexo = input("Ingrese el sexo(m , f , nb) ")
        if sexo == "m" or sexo == "f" or sexo == "nb":
            break
    
    while True:
        habilidad = input("Ingrese la habilidad(fuerza,magia o inteligencia) ")
        if habilidad == "fuerza" or habilidad == "magia" or habilidad == "inteligencia":
            break

    if habilidad == "fuerza": 
        if bandera_mas_joven == True: #A
            edad_mas_joven = edad
            nombre_mas_joven = nombre
            bandera_mas_joven = False
        elif edad_mas_joven > edad:
            edad_mas_joven = edad
            nombre_mas_joven = nombre

        if sexo == "m": #E
            edad_total_heroe_fuerza = edad_total_heroe_fuerza + edad
            contador_heroes_fuerza += 1
    
    if bandera_mas_viejo == True: #B
        edad_mas_viejo = edad
        sexo_mas_viejo = sexo
        nombre_mas_viejo = nombre
        bandera_mas_viejo = False
    elif edad_mas_viejo < edad:
        edad_mas_viejo = edad
        sexo_mas_viejo = sexo
        nombre_mas_viejo = nombre

    
    if sexo == "f":
        edad_total_heroina = edad_total_heroina + edad #d
        contador_de_heroinas += 1
        if habilidad == "fuerza" or habilidad == "magia": # c
            contador_de_heroinas_con_habilidades += 1

    respuesta = input("Si quiere seguir ingresando Heroes, escriba si ")

promedio_edad_heroinas = edad_total_heroina / contador_de_heroinas
promedio_edad_heroes = edad_total_heroe_fuerza / contador_heroes_fuerza
print("El nombre y la edad mas joven es: " , nombre_mas_joven , " con " , edad_mas_joven , " años")
print("El nombre y sexo del mas viejo es: ", nombre_mas_viejo , " y es " , sexo_mas_viejo)
print("La cantidad de heroinas con habilidades de fuerza o magia es: " , contador_de_heroinas_con_habilidades)
print("El promedio de edad entre heroinas es: ", promedio_edad_heroinas)
print("El promedio de edad entre heroes de fuerza es: ", promedio_edad_heroes)
