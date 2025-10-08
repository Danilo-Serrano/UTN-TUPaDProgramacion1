with open("producto.txt", "r") as archivo:
    for linea in archivo: 
        lineaStrip = linea.strip()
        lineaSplit = lineaStrip.split(",")
        print("Producto: ", lineaSplit[0], " | Precio: ", lineaSplit[1], " | Cantidad: ", lineaSplit[2] )

print("Ingresa un nuevo producto")
nombre = input("Agrega nombre del nuevo producto ")
precio = int(input("Agrega precio del nuevo producto "))
cantidad = int(input("Agrega cantidad del nuevo producto "))

with open("producto.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

productos=[]

with open("producto.txt", "r") as archivo:
    for linea in archivo: 
        lineaStrip = linea.strip()
        lineaSplit = lineaStrip.split(",")
        diccionario_prodcuto = {
            "nombre": lineaSplit[0],
            "precio": lineaSplit[1],
            "cantidad": lineaSplit[2]
        }
        productos.append(diccionario_prodcuto)
        print(productos)

buscar = input("Buscar elemento por nombre: ")

for producto in productos:
    if producto["nombre"] == buscar:
        boole = False
        print("producto encontrado, sus datos son: ", producto)
        break
    else:
        boole = True
        
if boole:
    print("ERROR Producto NO ENCONTRADO")
        