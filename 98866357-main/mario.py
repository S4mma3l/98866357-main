def main():
    print_column(3)


def print_column(height):
    print("#\n" * height, end="")


main()


def main():
    print_row(4)


def print_row(width):
    print("?" * width)


main()


def main():
    print_square(3)


def print_square(size):
    for i in range(size):  # para imprimir un bloque en la escuadra
        for j in range(size):  # para imprimir un bloque en la columna
            print("#", end="")  # impirme el bloque
        print()


main()


def main():
    print_square(3)


def print_square(size):
    for i in range(size):  # para imprimir un bloque en la escuadra
        print("#" * size)  # imprime el bloque


main()


def main():
    print_square(3)


def print_square(size):
    for i in range(size):  # para imprimir un bloque en la escuadra
        print_row(size)


def print_row(width):
    print("#" * width)


main()
