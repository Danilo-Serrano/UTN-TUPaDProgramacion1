# #1)
edad = int(input("Ingresa tu edad "))
if edad > 18:
    print("Es mayor de edad")
# #2)
nota = int(input("Ingresa una nota "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
#3)
num = int(input("Ingresa un número par o impar "))
if num % 2 == 0:
    print("Numero PAR")
else:
    print("Numero IMPAR")
#4)
edad = int(input("Ingresa tu edad "))
if edad < 12:
    print("Niño")
elif edad >= 12 and edad < 18:
    print("Adeloscente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")
#5)
contra = input("Ingresa contraseña entre 8 y 14 caracteres ")
long = len(contra)
if long >= 8 and long <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#7)
frase = input("Ingresa una frase o palabra: ")
ultima = frase[-1].lower()
if ultima in "aeiou":
    frase = frase + "!"
print(frase)
#8)
nombre = input("Ingresa tu nombre ")
num = int(input("1)pasar a mayusculas, 2)pasar a minusculas 3)primer letra mayuscula "))
if num == 1:
    print(nombre.upper())
elif num == 2:
    print(nombre.lower())
elif num == 3:
    print(nombre.capitalize())
else:
    print("Ingresa un número entreo 1 y 3")
#9)
magnitud=int(input("Ingresa magnitud del terremoto "))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")
#10)
hemisferio = input("Ingrese hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))
if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
else:
    estacion_norte = "Otoño"
if hemisferio == "N":
    estacion = estacion_norte
else:  
    if estacion_norte == "Invierno":
        estacion = "Verano"
    elif estacion_norte == "Verano":
        estacion = "Invierno"
    elif estacion_norte == "Primavera":
        estacion = "Otoño"
    else: 
        estacion = "Primavera"
print("Estás en:", estacion)
