golosinas = [
    [1, "Kitkat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix",10],
    [7, "MyMs", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

clavesTecnico=("admin", "CCCDDD", "2020")

golosinasPedidas = []


opcion = "b"

print("a)Pedir golosina b)Mostrar golosinas c)Rellenar golosinas d)Apagar maquina")

while opcion <= "d" and opcion >= "a":
    
    opcion = input("¿Qué deseas hacer? ")
    
    if opcion == "a":
        
        legajo = int(input("Ingresa tu legajo "))
        if legajo in empleados:
            print("Bienvenido, tiene acceso gratuito a las golosinas")
            eleccion_golosina = int(input("¿Que golosina buscas(ingresa su código) "))
            for i in range(12):
                if golosinas[i][0] == eleccion_golosina:
                    contador = 0
                    if golosinas[i][2] > 0:
                        contador = contador + 1
                        print("Golosina encontrada", golosinas[i][1])
                        golosinas[i][2] -= 1
                        print("Stock restante: ", golosinas[i][2])
                        
                        for j in range(len(golosinasPedidas)):
                            if golosinasPedidas[j][0] == golosinas[i][0]:
                                golosinasPedidas[j][2] += 1
                                break
                        else:
                            pedidas = [golosinas[i][0], golosinas[i][1], 1]
                            golosinasPedidas.append(pedidas)
                        
                    else:
                        print("Lo sentimos la golosina ", golosinas[i][1],  " no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina")
                        break
        else:
            print("Usted no es un empleado de la empresa")
            
    elif opcion == "b":
        print(golosinas)
    elif opcion == "c":
        print("Ingresa contraseña de 3 pasos")
        pal1 = input("1 palabra ")
        pal2 = input("2 palabra ")
        pal3 = input("3 palabra ")
        if pal1 == clavesTecnico[0] and pal2 == clavesTecnico[1] and pal3 == clavesTecnico[2]:
            print("Bienvenido Jefe")
            codigo_agregar_golosinas = int(input("Ingresa el código de la golosina que quieres agregar " ))
            for i in range(12):
                if golosinas[i][0] == codigo_agregar_golosinas:
                    cantidad = input("Ingresa la nueva cantidad de ")
                    golosinas[i][2] = cantidad
                    print(golosinas)
                    
        else:
            print("No tiene permiso para ejecutar la función de recarga ")
    elif opcion == "d":
        print("Historial de compras de hoy")
        print(golosinasPedidas)
        acum = 0
        for pedido in golosinasPedidas:
            acum += int(pedido[2])
            
        print("Se compraron", acum, "GOLOSINAS hoy")
        break
    else:
        pass