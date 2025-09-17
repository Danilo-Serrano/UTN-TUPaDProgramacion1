#ejercicio 1
for num in range(101):
    if num % 4 == 0:
        print(num)
#ejercicio 2
array = []
for i in range(5):
    item = input("Ingresa 5 elementos al array ")
    array.append(item)
print("el penúltimo elemento es: ", array[-2])
#ejercicio 3
array = []
for i in range(3):
    item = input("Ingresa 3 elementos al array ")
    array.append(item)
print(array)
#ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
for i in animales:
    animales[1] = "loro"
    animales[-1] = "oso"
print(animales)
#ejercicio 5
#El programa elimina el número más alto del array y después muestra el array sin el número máximo
#ejercicio 6
for i in range(10, 31, 5):
    if i < 20:
        print(i)
#ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "bora"
autos[2] = "vento"
print(autos)
#ejercicio 8
dobles = []
normal = [5,10,15]
for i in normal:
    itemDoble = i * 2
    dobles.append(itemDoble)
print(dobles)
#ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].pop(0)
print(compras)
#ejercicio 10
lista_anidada = [
    15, True, [25.5, 57.9, 30.6], False
]
print(lista_anidada)