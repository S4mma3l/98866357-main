# x = 1
# y = 2

x = input("Que es X? ")
y = input("Que es Y? ")

z = int(x) + int(y) # para coventir en un numero entero debo de agregar la funcion "int" se puede hacer de esta forma


print (z)

# segunda opcion para poder hacer las funcion numero enteros

x = int(input("Que es X? "))
y = int(input("Que es Y? "))

print( x + y )

# opcion para hacer la funcion con numero flotantes (float)

x = float(input("Que es X? "))
y = float(input("Que es Y? "))

print( x + y )

# opcion 2 para hacer la funcion con numero flotantes (float) con redondeo (round)

x = float(input("Que es X? "))
y = float(input("Que es Y? "))

z = round(x + y)

print(z)
print(f"{z:,}") # Con esta opcion podemos colocas una coma adelante para realizar una disticion

x = float(input("Que es X? "))
y = float(input("Que es Y? "))

z = x / y
z = round(x / y, 2) # Forma numero 1 de imprimir solos 2 digitos

print(z)

print(f"{z:.2f}") # Forma numero 2 de imprimir solos 2 digitos