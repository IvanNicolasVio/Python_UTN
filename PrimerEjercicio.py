'''
Vio Ivan Nicolas (Ejercicio hecho en clase)

La división de higiene está trabajando en un control de stock para productos sanitarios. 
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
El tipo (validar "barbijo", "jabón" o "alcohol")
El precio: (validar entre 100 y 300)
La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
La marca y el Fabricante.
  
 Se debe informar lo siguiente:
Del más caro de los barbijos, la cantidad de unidades y el fabricante.
Del ítem con más unidades, el fabricante.
Cuántas unidades de jabones hay en total.
'''

precio_barbijo_caro = -1
cantidad_jabones = 0
items_mas_unidades = -1

for iteracion in range(5):

    tipo_producto = input("ingrese el tipo de producto (jabon,barbijo,alcohol) ") #VALIDACION DE DATOS
    while tipo_producto != "jabon" and tipo_producto != "barbijo" and tipo_producto != "alcohol":
        tipo_producto = input("ingrese el tipo de producto(jabon,barbijo,alcohol) ")

    while True: #DO WHILE VERSION UTN
        precio = int(input("Ingrese el precio(Entre 100 y 300) "))
        if precio > 99 and precio < 301:
            break

    while True: #DO WHILE VERSION UTN
        cantidad = int(input("Ingrese la cantidad(Entre 1 y 1000) "))
        if cantidad > 0 and cantidad < 1000:
            break

    marca = input("Ingrese la marca ")

    fabricante = input("Ingrese el fabricante ")

    if tipo_producto == "barbijo": #Del más caro de los barbijos, la cantidad de unidades y el fabricante.
        if precio > precio_barbijo_caro:
            precio_barbijo_caro = precio
            cantidad_barbijo_caro = cantidad
            fabricante_barbijo_caro = fabricante
    elif tipo_producto == "jabon":#Cuántas unidades de jabones hay en total.
        cantidad_jabones += cantidad
    

    if cantidad > items_mas_unidades:
        items_mas_unidades = cantidad
        fabricantes_mas_unidades = fabricante


print("La cantidad de barbijos caros es de : " , cantidad_barbijo_caro , " lo fabrica: ", fabricante_barbijo_caro)
print("El fabricante del item con mas unidades es: " , fabricantes_mas_unidades)
print("Cantidad de jabones: " , cantidad_jabones)


    

    
    

    



