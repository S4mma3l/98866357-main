def main():
    x = int(input("Que es X? "))
    print("X squared is", square(x))

def square(n):
    #return n * n # forma 1 
    return n ** 2 # forma 2
    #return pow(n, 2) # forma 3

main()