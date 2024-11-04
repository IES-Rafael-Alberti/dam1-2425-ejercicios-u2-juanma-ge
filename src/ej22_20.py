def pedir_frase():
    return input("Introduce una frase: ")

def pedir_letra():
    return input("Introduce una letra a buscar: ")

def buscar_letra(frase, letra):
    for indice, caracter in enumerate(frase):
        if caracter == letra:
            print(f"Se encontró la letra '{letra}' en la posición {indice}.")
            return  # Finaliza la ejecución al encontrar la letra
        else:
            print(f"No hay coincidencia en la posición {indice}.")
    print(f"La letra '{letra}' no se encontró en la frase.")

def main():
    frase = pedir_frase()
    letra = pedir_letra()
    
    if len(letra) != 1:
        print("Por favor, introduce solo una letra.")
        return
    
    buscar_letra(frase, letra)

if __name__ == "__main__":
    main()
