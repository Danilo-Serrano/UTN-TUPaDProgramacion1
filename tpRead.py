# funciones
def ver_alumnos():
    with open("alumnos.txt", "r") as archivo:
        for linea in archivo:
            alumnos_strip = linea.strip()
            alumnos_split = alumnos_strip.split(";")
            print(alumnos_split)

def agregar_alumno():
    with open("alumnos.txt", "a") as archivo:
        while True:
            nombre = input("Agrega nombre del nuevo alumno ")
            if nombre.lower() == "salir":
                print("Saliendo de Agregar alumnos...")
                break
            elif nombre == "" or nombre.isdigit():
                print("Nombre no válido")
                print("Ingresa un nombre válido o pon 'salir'")
                continue
            else:
                break
            
        while True:
            apellido = input("Agrega apellido del nuevo alumno ")
            if apellido.lower() == "salir":
                break
            elif apellido == "" or apellido.isdigit():
                print("Apellido no válido")
                print("Ingresa un apellido válido o pon 'salir'")
                continue
            else:
                break
        
        while True:
            legajo = input("Agrega legajo del nuevo alumno ")
            if legajo.lower() == "salir":
                break
            elif legajo == "" or not legajo.isdigit() or len(legajo) != 5:
                print("Legajo no válido")
                print("Ingresa un legajo válido o pon 'salir'")
                continue
            else:
                break
            
        while True:
            promedio = int(input("Agrega promedio del nuevo alumno "))
            if promedio >= 1 and promedio <= 10:
                archivo.write(f"{nombre};{apellido};{legajo};{promedio}\n")
                break
            else:
                print("Pon un promedio entre 1 y 10")
                
def generar_aprobado():
    with open("alumnos.txt", "r") as archivo:
        for linea in archivo:
            linea_strip = linea.strip()
            linea_split = linea_strip.split(";")
            nota = int(linea_split[-1])
            if nota >= 6:
                with open("alumnosAprobados.txt", "a") as archivo:
                    archivo.write( f'{linea_split}, \n ')
                    print(linea_split)
# Inicio Programa
opcion = 1
while opcion != 4:
    print("1-Ver alumnos\n2-Agregar Alumno\n3-Generar y mostrar archivo de aprobados\n4-Salir ")
    opcion = int(input("¿Qué desea hacer? "))
    if opcion == 1:
        ver_alumnos()
    if opcion == 2:
        agregar_alumno()
    if opcion == 3:
        generar_aprobado()