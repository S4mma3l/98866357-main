x = int(input("Que es X? "))
y = int(input("Que es Y? "))
# primera opcion con if
if x < y: #Simbolo de menor < aca tambien usamos la variable de if que se representa como si (if) esto es....
    print("X es Menor (<) que Y")

if x > y: #Simbolo de Mayor >
    print("X es Mayor (>) que Y")

if x == y: # Simbolo de igualdad == / de esta forma con if el programa realiza la pregunta tres veces 
    print("X es Igual (==) que Y")

# segunda opcion con elif
if x < y: #Simbolo de menor </ 
    print("X es Menor (<) que Y")

elif x > y: #Simbolo de Mayor > / aca tambien usamos la variable de elif y de esta forma si una repuesta es corecta solo calcula la preunta correcta no ejecuta las tres
    print("X es Mayor (>) que Y")

elif x == y: # Simbolo de igualdad ==
    print("X es Igual (==) que Y")

# Tercera opcion con else
if x < y: #Simbolo de menor </ 
    print("X es Menor (<) que Y")

elif x > y: #Simbolo de Mayor > 
    print("X es Mayor (>) que Y")

else: # Simbolo de igualdad ==
    print("X es Igual (==) que Y")

# Tercera opcion con or que se puede representar en lenguje normal o
if x < y or x > y:
    print("X no es igual que Y")

else: # Simbolo de igualdad ==
    print("X es Igual (==) que Y")

#  Cuarta opcion se puede cambiar por el simbolo de no igualdad !=
if x != y:
    print("X no es igual que Y")

else: # Simbolo de igualdad ==
    print("X es Igual (==) que Y")