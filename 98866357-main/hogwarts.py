# froma de interactuar lista con buclea forma 1
estudiante = ["Hermione", "Harry", "Ron"]

print(estudiante[0])
print(estudiante[1])
# dentro del codigo podemos realizar la impresion de una forma rudimentaria como esta o podemos hacer un bucle como el siguiente
print(estudiante[2])

for alumno in estudiante:
    print(alumno)

# forma de interactuar lista con bucles forma 2

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(
        student, students[student], sep=", "
    )  # de esta forma podemos vincular a partir de una lista los nombres y la casa de cada uno.

# forma de interactuar lista con bucles forma 3
# con esta opcion se puede de un diccionario dentro de una lista obtener los datos atraves de un bucle

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russel Terrier",
    },  # esto es un diccionario dentro de una lista
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(
        student["name"], student["house"], student["patronus"], sep=", "
    )  # se maneja la informacion de esta manera
