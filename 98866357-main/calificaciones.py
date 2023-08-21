calificacion = int(input("Calificacion: "))

# Primera forma de hacer el programa
if calificacion >= 90 and calificacion <= 100:
    print("Calificacion: A")

elif calificacion >= 80 and calificacion <= 90:
    print("Calificacion: B")

elif calificacion >= 70 and calificacion <= 80:
    print("Calificacion: C")

elif calificacion >= 60 and calificacion <= 70:
    print("Calificacion: D")

else:
    print("Calificacion: F")

# Segunda forma de hacer el programa
if 90 <= calificacion <= 100:
    print("Calificacion: A")

elif 80 <= calificacion < 90:
    print("Calificacion: B")

elif 70 <= calificacion < 80:
    print("Calificacion: C")

elif 60 <= calificacion < 70:
    print("Calificacion: D")

else:
    print("Calificacion: F")

# Tercera forma de hacer el programa / de esta forma seria la mejor opcion para crear el programa de una forma limpia
if calificacion >= 90:
    print("Calificacion: A")

elif calificacion >= 80:
    print("Calificacion: B")

elif calificacion >= 70:
    print("Calificacion: C")

elif calificacion >= 60:
    print("Calificacion: D")

else:
    print("Calificacion: F")
