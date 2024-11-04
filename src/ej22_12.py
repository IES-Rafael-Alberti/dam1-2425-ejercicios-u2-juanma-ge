def pedir_letra():
    return input("Introduce una letra: ")

def pedir_frase():
    return input("Introduce una frase: ")

def hacer_frase(frase, letra):
    frase2 = frase.count(letra)
    print(frase2)

def main():
    letra = pedir_letra()
    frase = pedir_frase()
    hacer_frase(frase, letra)

if __name__ == "__main__":
    main()