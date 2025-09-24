#1)
precios_frutas = {'Banana': 1200,
                    'Ananá': 2500, 
                    'Melon': 3000, 
                    'Uva':1450
                }
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)
#2)
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800
print(precios_frutas)
#3)
claves =precios_frutas.keys()
nuevo_array = []
nuevo_array.extend(claves)
print(nuevo_array)
# 4)
telefono = {}
for i in range(5):
    nombre = input("ingesa nombre del contacto ")
    numero = input("ingesa numero del contacto ")
    telefono[nombre] = numero
    
telefono_a_buscar = input("Ingresa el nombre de la persona que buscas: ")
if telefono_a_buscar in telefono:
    print("El número de esa persona es: "+telefono[telefono_a_buscar])
else:
    print("No se encontró ese nombre en los contactos")
#5)
frase = input("Ingrese una frase: ")
palabras = frase.split()
print("Palabras únicas:", set(palabras))
print("Cantidad de veces que aparece cada palabra:")
for palabra in set(palabras):
    print(palabra, ":", palabras.count(palabra))
#6)
alumnos = {}
for i in range(3):
    nombre = input("ingresa un nombre "), 
    nota1 = int(input("Ingresa nota 1: "))
    nota2 = int(input("Ingresa nota 2: "))
    nota3 = int(input("Ingresa nota 3: "))
    notas = (nota1, nota2, nota3)
    porcentaje = (nota1 + nota2 + nota3) / 3
    alumnos[nombre] = notas
    print("Alumno: " , nombre, " Notas: " , notas, " promedio: ", porcentaje)
#7)
parcial1 = set()
parcial2 = set()
for i in range(3):
    alumno1 = input("Alumno que aprobó el primer parcial: ")
    parcial1.add(alumno1)
for i in range(3):
    alumno2 = input("Alumno que aprobó el segundo parcial: ")
    parcial2.add(alumno2)
ambos = []
for alumno in parcial1:
    if alumno in parcial2:
        ambos.append(alumno)
print("Aprobaron ambos parciales:", ambos)
solo_uno = []
for alumno in parcial1.union(parcial2):  
    if (alumno in parcial1) != (alumno in parcial2):
        solo_uno.append(alumno)
print("Aprobaron solo uno de los parciales:", solo_uno)
al_menos_uno = list(parcial1)
for alumno in parcial2:
    if alumno not in al_menos_uno:
        al_menos_uno.append(alumno)
print("Aprobaron al menos un parcial:", al_menos_uno)
#8)
productos = {
    "pan": 10,
    "leche": 5,
    "carne":25
}
opcion = 2
while opcion <= 2 and opcion >=1: 
    opcion = int(input("1-Consulta stock 2-Agregar unidades al stock del producto existente 3-Terminar programa "))
    if opcion == 1:
        consultar_stock = input("Sobre q produco quieres saber el stock? ")
        print(productos.get(consultar_stock))
    elif opcion == 2:
        stock_a_ingresar = input("A q producto quieres agregarle stock?")
        if stock_a_ingresar in productos:
            print("este producto si existe ")
            nuevo_stock = input("Agregar nuevo stock ")
            productos[stock_a_ingresar] = nuevo_stock
        else:
            print("ese producto no existe, crea uno nuevo")
            nuevo_producto = input("Agrega un nuevo producto ")
            nuevo_producto_stock = input("Agrega un nuevo stock ")
            productos[nuevo_producto] = nuevo_producto_stock
print(productos)
# 9)
agenda = {
    ("lunes", "10"): "Reunión",
    ("martes", "15"): "Clase de inglés",
    ("miércoles", "09"): "Gimnasio",
    ("jueves", "14"): "Almuerzo con amigos",
    ("viernes", "11"): "Entrega de proyecto",
    ("sabado", "16"): "Cine",
    ("domingo", "12"): "cena familiar"
}
dia = input("Ingresa el día: ")
hora = input("Ingresa la hora: ")
clave = (dia, hora)
if clave in agenda:
    print(f"En {dia} a las {hora} hay: {agenda[clave]}")
else:
    print(f"No hay actividades registradas para {dia} a las {hora}.")
#10)
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}
capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais
print(capitales_paises)

    
    