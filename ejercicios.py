# Danilo Serrano 1PRO1

print("Hola Mundo!")

nombre = input("Ingresa tu nombre ")
print("Hola " + nombre)

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
print("Soy " + nombre + " " + apellido + " tengo " + edad + " años y vivo en " + residencia)

pi = 3.1416
radio = float(input("Ingresa el radio del círculo: "))
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

segundos =float(input("Ingresa segundos: "))
horas = segundos / 3600
print(str(segundos) + " equivale a: " + str(horas) + " horas")

numero = int(input("Número: "))
print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

a = int(input("Primer número: "))
b = int(input("Segundo número: "))

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

Imc = peso / (altura * altura)
print("IMC:", Imc)

celssius = float(input("Temperatura en °C: "))
fahrenheit = (9 / 5) * celssius + 32
print("Equivalente en °F:", fahrenheit)

x = float(input("Primer número: "))
y = float(input("Segundo número: "))
z = float(input("Tercer número: "))

promedio = (x + y + z) / 3
print("Promedio:", promedio)
