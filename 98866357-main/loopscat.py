# con este programa vamos a usar lo bucles or loops desde una manera muy simple hasta a forma adecuada de hacerlo

print("meow")
print("meow")
print("meow")

# Palabra de sistema "while"

i = 3
while i != 0:  # != diferente o igual
    print("meow")  # esta seria una opcion de hacer el programa
    i = i - 1

i = 0
while i < 3:  # < menor
    print("meow")  # aca seria ona segunda opcion de realizar el mismo program
    i += 1


# Palbara de sistema "for" y lstas

for i in [0, 1, 2,]:
    print("meow")

print("meow" * 3)  # podemos realizar de esta forma pero nos queda en una sola line
# lo podemos solucionar escapando en la zona de meow con "\n" pero nos brinca un salto de linea extra
print("meow\n" * 3)
print("meow\n" * 3, end="")  # y de esta forma podemos realizar con la misma opcion del salto de linea "\n" pero agremos "end = """ para quitar el salto de linea extra

# Paradigma comun en python

while True:
    # en esta zona tenemos un bucle que se repite constatemente si la respuesta es un numero negativo
    n = int(input("Cuantas veces maulla el gato? "))
    # al ingresar un numero valido se contunua a la siguiente parte del programa
    if n > 0:
        break

for _ in range(n):
    print("meow")

#  Podemos realizar todo este proceso atraves de una funcion


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("Cuantas veces maulla el gato? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
