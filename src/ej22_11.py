def pedir_palabra(): 
    return input("Introduce una palabra: ")

def separar_letras(palabra):
    for letra in reversed(palabra):
        print(letra)

def main():
    palabra = pedir_palabra()
    separar_letras(palabra)

if __name__ == "__main__":
    main()