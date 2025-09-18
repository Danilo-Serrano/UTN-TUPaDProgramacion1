# TP Funciones
# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, lugar):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, lugar)

# Ejercicio 4
import math
def calcular_area(radio):
    return math.pi * radio ** 2

def calcular_perimetro(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
print("Área:", calcular_area(radio))
print("Perímetro:", calcular_perimetro(radio))


# Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print("Equivale en horas a:", segundos_a_horas(segundos))


# Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para su tabla de multiplicar: "))
tabla_multiplicar(numero)

# Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return suma, resta, multiplicacion, division

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

suma, resta, multiplicacion, division = operaciones_basicas(a, b)

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print("Su IMC es:", round(calcular_imc(peso, altura), 2))

# Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en Celsius: "))
print("Equivalente en Fahrenheit:", celsius_a_fahrenheit(celsius))

# Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
print("El promedio es:", calcular_promedio(a, b, c))