x = int(input("Que numero es X? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")


# Podria realizar esta operacion en una funcion de esta forma

def main():
    x = int(input("Que numero es X? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True            # esta funcion se puede relizar de esta forma
    else:
        return False


def is_even(n):
    return True if n % 2 == 0 else False  # o de esta manera


def is_even(n):
    return n % 2 == 0  # y tambien de esta otra todas son correctas.


main()


#  match es un mecanismo
