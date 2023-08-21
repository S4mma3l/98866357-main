name = input("Cual es tu nombre? ")


if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    # Este programa Funciona de esta manera y es la forma mas larga de hacerlo
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")


if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":                   # esta seria una segunda opcion de hacer este programa un poco mas pequena
    print("Slytherin")
else:
    print("Who?")


# Aca vamos a usar una nueva funcion llamada "match"

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:   # Con guion bajo se usa en este caso para darle un valor de que cualquier dato ingresado que no sea de los anteriores de ese esta condicional
        print("Who?")


match name:
    case "Harry" | "Hermione" | "Ron":  # de esta forma como con if lo podemos unificar pero de una forma las limpia solo con |
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:   # Con guion bajo se usa en este caso para darle un valor de que cualquier dato ingresado que no sea de los anteriores de ese esta condicional
        print("Who?")
