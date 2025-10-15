#Ejercicio 1
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
numero = int(input("Escriba un nùmero lìmite entre 1 y 10, para sacar sus factoriales: "))
for i in range(numero,0,-1):
    print(factorial(i))
#Ejercicio 2
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        temp = a
        a = b
        b = temp + b
fibonacci(10)
fibo = int(input("Ingresa la posiciòn final de la secuencia fibonacci"))
#Ejercicio 3
def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp -1)
b = int(input("Ingresa la base: "))
e = int(input("Ingresa elexponente: "))
print(potencia(b,e))
#Ejercicio 4
num = int(input("Ingresa un nùmero para pasarlo a binario "))
def convertir(num):
    if num == 0:
        return ""
    else:
        return convertir(num // 2) + str(num % 2)
binario = convertir(num)
print(num, " en binario es: ", binario)
#Ejercicio 5
palabra = input("Ingresa una palabra: ")
for letra in palabra:
    if letra == " " or letra in "áéíóúÁÉÍÓÚ":
        print("Debes ingresar una palabra sin espacios ni tildes")
a = 0
b = len(palabra) -1
def paliondromo(a,b, palabra):
    for i in range(0, len(palabra)):
        if palabra[a] == palabra[b]:
            a += 1
            b -= 1
        else:
            return "Esta palabra no es palindroma"
    return "Esta palabra SI es palindroma"
paliondromo(a,b, palabra)
print(paliondromo(a,b,palabra))
#Ejercicio 6
def suma(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + suma(num // 10)
num = int(input("Qué numero quieres sumar? "))
print(suma(num))
#Ejercicio 7
base = int(input("Ingresa base de la piramide "))

def piramide(base):
    if base == 1:
        return 1
    else:
        return base + piramide(base - 1)
    
print(piramide(base))
#Ejercicio 8
def contar_digito(num,dig):
    if num == 0:
        return 0
    if num % 10 == dig:
        return 1 + contar_digito(num // 10, dig)
    else:
        return contar_digito(num // 10, dig)
num = int(input("Ingresa numeros "))
dig = int(input("Ingresa un dígito "))
if dig <= 9 and dig >= 0:
    print("El dígito ", dig, " aparece ",contar_digito(num,dig), " veces en el número ingresado")
