try:                                      # try es una palabra del sistema que intenta solucionar un problema
    x = int(input("Que numero es? "))
    print(f"X es {x}")
except ValueError:                        # con la palabra except validamos que al tener un error nos indique que debemos de hacer
    # se soluciona el erros de valor ValueError
    print("X no es un entero")


try:
    x = int(input("Que numero es? "))
except ValueError:
    print("X no es un entero")
else:                                     # con la palabra else podremos solucionar un error de NameError ya que le decimos al programa que si ocurre este  pase a mi exception
    print(f"X es {x}")

while True:
    try:
        x = int(input("Que numero es? "))
    except ValueError:
        print("X no es un entero")
    else:                                # podriamos realizar un bucle while con la sintasis anterior pero realizando un break  despues del else creando un codigo mas limpio
        break
print(f"X es {x}")


def main():
    x = get_int()
    print(f"X is {x}")


def get_int():
    while True:
        try:
            return int(input("Que numero es? "))
        except ValueError:
            # podriamos realizar todo el proceso atravez de una funcion y while con la misma sintaxis anterior pero sin un break podria ser mas limpio
            print("X no es un entero")


main()


def main():
    x = get_int()
    print(f"X is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:     # podriamos realizar todo el proceso atravez de una funcion y while con la misma sintaxis anterior pero con un pass que no imprime el error en pantalla ni otra cosa
            pass


main()
