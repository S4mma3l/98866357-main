# Preguntar por sus nombres
name = input("Cual es tu nombre? ").strip().title() # de esta forma puedo unificar toda lo que veo abajo

# Eliminar los espacios que el usuario pueda ingresar en una str =

# name = name.strip()# Con esta funcion puedo eliminar los espacios que ingrese el usuario

# Capitalize el nombre del usuario

# name = name.capitalize() # Con esta funcionpuedo colocar en mayuscula la primera letra

# name = name.title()  # Con esta funcion pongo mayusculas solo a los inicios de cada palabra

# Separa user's name into first name and last name

first, last = name.split(" ")

# Di Hola
print("Hello, ", name, sep="***") # Generar un espacio sin la necidad de dar el espacio en el codigo
print("Hello, " + name)
print("Hello, ", end="&&&") # funcion end para evitar en escape a otra linea
print(name)
print("Hello, ")
print(name)
print("hello, \"Amigo\"") # de esta forma se puede ingresar doble comillas sin que afecte las doble caillas originales
print(f"Hello, {first} {last}") # esta es una forma adecuada del formato de una string