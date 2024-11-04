def obtener_frase():
    """Solicita al usuario que ingrese una frase y la retorna."""
    frase = input("Por favor, ingrese una frase: ")
    return frase

def contar_palabras(frase):
    """Cuenta el número de palabras en la frase."""
    # Se separa la frase por espacios y se filtran los elementos vacíos
    palabras = [palabra for palabra in frase.split() if palabra]
    return len(palabras), palabras

def encontrar_palabra_mas_larga(palabras):
    """Encuentra la palabra más larga en la lista de palabras."""
    if not palabras:
        return None
    palabra_mas_larga = max(palabras, key=len)
    return palabra_mas_larga

def main():
    """Función principal que ejecuta el programa."""
    frase = obtener_frase()
    cantidad_palabras, palabras = contar_palabras(frase)
    palabra_mas_larga = encontrar_palabra_mas_larga(palabras)
    
    print(f"Cantidad de palabras: {cantidad_palabras}")
    if palabra_mas_larga:
        print(f"La palabra más larga es: '{palabra_mas_larga}'")

main()
