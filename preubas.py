alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

materias = ["Ciencias", "Historia", "Geografía", "Matemáticas", "Física"]

# Lista para guardar el promedio final de cada alumno
notasFinales = []

for alumno in alumnos.values():
    print(f"\nAlumno: {alumno}")
    materias_cargadas = []  # lista de [materia, nota1, nota2, promedio]
    promedios = []  # para calcular el promedio general

    for materia in materias:
        print(f"\nIngrese las notas para la materia {materia}")

        # Validación de nota 1
        while True:
            nota1 = float(input("Nota 1: "))
            if 0 <= nota1 <= 10:
                break
            print("❌ La nota debe estar entre 0 y 10.")

        # Validación de nota 2
        while True:
            nota2 = float(input("Nota 2: "))
            if 0 <= nota2 <= 10:
                break
            print("❌ La nota debe estar entre 0 y 10.")

        promedio = (nota1 + nota2) / 2
        print(f"Nota Final: {promedio}\n")

        materias_cargadas.append([materia, nota1, nota2, promedio])
        promedios.append(promedio)

    # Mostrar materias completas
    print("\n--- Materias cargadas ---")
    for m in materias_cargadas:
        print(m)

    # Determinar la mejor materia
    mejor_materia = max(materias_cargadas, key=lambda x: x[3])
    print(f"\n📘 La mejor materia de {alumno} fue {mejor_materia[0]} con promedio {mejor_materia[3]}")

    # Calcular promedio general del alumno
    promedio_general = sum(promedios) / len(promedios)
    print(f"📊 Promedio general de {alumno}: {promedio_general}")

    # Guardar en notasFinales
    notasFinales.append([alumno, promedio_general])

# Mostrar resumen final
print("\n===== Promedios Finales =====")
for registro in notasFinales:
    print(f"{registro[0]} → {registro[1]}")

# Determinar mejor alumno
mejor_alumno = max(notasFinales, key=lambda x: x[1])
print(f"\n🏆 El mejor promedio fue de {mejor_alumno[0]} con {mejor_alumno[1]}")
