#ejerciio 1
for i in range(101):
    print(i)
#ejercicio 2
num = input("Ingresa un número ")
for i in num:
    pass
num =-1
print("el número ingresado tiene ", i, " dígitos")
#ejercicio 3
valor1 = int(input("Ingresa el primer número: "))
valor2 = int(input("Ingresa el segundo número: "))
inicio = min(valor1, valor2)
fin = max(valor1, valor2)
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print(f"La suma de los números entre {inicio} y {fin}, es: {suma}")
#ejercicio 4
total = 0
num = 1
while num != 0:
    num = int(input("Ingresa un número "))
    total = total + num
print("La suma de los números ingresados es: ", total)
#ejercicio 5
import random
num = -1
cont= 0
aleatorio = int(random.uniform(0, 10))
print(aleatorio)
while num != aleatorio:
    num = int(input("adivina el numero "))
    cont = cont + 1
print("Adivinaste el número ")
print("Tardaste ", cont, " intentos")
#ejercicio 6
for i in range(100, 0, -1):
    if i % 2 == 0:
        print(i)
#ejercicio 7
total = 0
num = int(input("Ingresa el número límite: "))
for i in range(0, num + 1, 1):
    total = total + i

print("La suma entre 0 y", num, "es:", total)
#ejercicio 8
CANTIDAD = 10
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(CANTIDAD):
    num = int(input(f"Ingrese el número {i + 1}: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("\n--- Resultados ---")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
#ejercicio 9
CANTIDAD = 10
suma = 0
for i in range(CANTIDAD):
    num = int(input(f"Ingrese el número {i + 1}: "))
    suma += num

media = suma / CANTIDAD
print("\nLa media de los", CANTIDAD, "números ingresados es:", media)
#ejercicio 10
numero = input("Ingresa un número: ")
if numero[0] == "-":
    invertido = "-" + numero[:0:-1]
else:
    invertido = numero[::-1]
print("Número invertido:", invertido)

