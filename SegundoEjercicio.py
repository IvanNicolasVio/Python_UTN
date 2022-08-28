'''
La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para la cocina de Industrias Wayne. 
Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
PESO: (entre 10 y 100 kilos)
PRECIO POR KILO: (mayor a 0 [cero]).
TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto. 
o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
El importe total a pagar, BRUTO sin descuento.
El importe total a pagar con descuento (Solo si corresponde).
Informar el tipo de alimento más caro.
El promedio de precio por kilo en total.

Vio Ivan Nicolas

'''
respuesta = "si"
total_de_kilos = 0
total_a_pagar = 0
precio_mas_alto = -1


while respuesta == "si":
    while True:
        peso = int(input("Ingrese el peso(entre 10 y 100kilos) "))
        if peso > 9 and peso < 101:
            break

    while True:
        precio_por_kilo = int(input("Ingrese el precio por kilo(mayor a 0) "))
        if precio_por_kilo > 0:
            break

    while True:
        tipo = input("Ingrese el tipo(v, a , m) ")
        if tipo == "v" or tipo == "a" or tipo == "m":
            break

    total_de_kilos = total_de_kilos + peso
    total_a_pagar = total_a_pagar + precio_por_kilo

    if precio_mas_alto < precio_por_kilo:
        precio_mas_alto = precio_por_kilo
        tipo_alimento_mas_caro = tipo

    respuesta = input("Si quiere ingresar mas datos ponga si")


promedio = total_a_pagar / total_de_kilos #promedio de precio por kilo

if total_de_kilos > 299: #va afuera del while
    descuento = 0.25
elif total_de_kilos > 99:
    descuento = 0.15
else:
    descuento = 0

descuento_final = total_a_pagar * descuento #va afuera del while
total_a_pagar_con_descuento = total_a_pagar - descuento_final

print("El importe bruto es $" , total_a_pagar)
if descuento == 0:
    print("NO HAY DESCUENTO")
    print("No hay importe con descuento")
else:
    print("El descuento es del ", descuento * 100 , "%")
    print("El importe con descuento es $" , total_a_pagar_con_descuento)
if tipo_alimento_mas_caro == "v":
    print("El tipo de alimento mas caro es: Vegetal")
elif tipo_alimento_mas_caro == "a":
    print("El tipo de alimento mas caro es: Animal")
else:
    print("El tipo de alimento mas caro es: Mezcla")
print("El promedio de precio por kilo es: $" , promedio)
