#!/usr/bin/env python3

'''# Preguntar por el nombre
name = input("Cual es tu nombre? ").strip().title()

# Di hola a el usuario
print(f"Hello, {name}")'''


# Crear un saludo atraves de una funcion
def hello(to="World"): # de esta forma podemos generar un saludo general llamando mas abajo y ademas un saludo personalizado
    print("Hello,", to)

hello() # saludo general
name = input("Cual es tu nombre? ").title()
hello(name) # saludo personalizado

# Crear una funcion que se pueda llamar desde cualquier punto
def main():
    name = input("Cual es tu nombre? ").title()
    hello(name) # saludo personalizado

def hello(to="World"): 
    print("Hello,", to)

main()
