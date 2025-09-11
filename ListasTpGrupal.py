#ejercicio 3
lista = []
for i in range(5):
    lista.append(input("Ingresa un elemento en la lista ")) 
print(lista)
# ejercicio 6
lista = []
for i in range(5):
    lista.append(input("Ingresa un elemento en la lista ")) 
    lista_sin_duplicados = set(lista)
print(lista_sin_duplicados)
#ejercicio 9
lista = []
lista_primos = []
for i in range(5):
    num = int(input("Ingresa un elemento en la lista: "))
    lista.append(num)
    if num > 1:
        for j in range(2, num):
            if num % j == 0:
                break
        else:
            lista_primos.append(num)
print("Lista Entera:", lista)
print("Números primos:", lista_primos)
#ejercicio 12
lista_1 = []
lista_2 = []
lista_resultado = []
for i in range(5):
    num = int(input("Ingresa un elemento en la lista1: "))
    lista_1.append(num)

for i in range(5):
    num = int(input("Ingresa un elemento en la lista2: "))
    lista_2.append(num)

for i in range(5):
    suma = lista_1[i] + lista_2[i]
    lista_resultado.append(suma)

print("La suma entre items de la lista 1 y 2 da:", lista_resultado)
#ejercicio 15
bidimensional = [
    [1,2,3],
    [4,20,6],
    [7,8,9]
]
suma = 0
for i in  bidimensional:
    for elemento in i:
        suma += elemento
print(suma)
#ejercicio 18
bidimensional = [
    [1,97,3],
    [4,20,6],
    [7,8,1]
]
num_menor = -99
for i in bidimensional:
    for j in i:
        if j > num_menor:
            num_menor = j
        
print("El número mayor de la lista bidimensional es: ", num_menor)
#ejercicio 21
n = int(input("Ingresa tamaño de la matriz "))
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)
for fila in matriz:
    print(' '.join(str(x) for x in fila))
#ejercicio 24
bidimensional = [
    [1,2,3],
    [4,20,6],
    [7,8,16]
]
n = len(bidimensional)
matriz_rotada = []
for j in range(n):
    nueva_fila = []
    for i in range( n - 1, -1, -1):
        nueva_fila.append(bidimensional[i][j])
    matriz_rotada.append(nueva_fila)
    
for fila in matriz_rotada:
    print(" ".join(str(x) for x in fila))