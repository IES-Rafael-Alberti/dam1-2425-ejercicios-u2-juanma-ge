def hacer_burbuja(lista):
    """
    Ordena una lista de números utilizando el algoritmo de ordenamiento burbuja.
    Compara cada par de elementos adyacentes en la lista y los intercambia si están
    en el orden incorrecto. Este proceso se repite hasta que la lista esté completamente ordenada.

    Parámetros:
        lista (list): Una lista de números a ordenar.
    
    Devuelve:
        None: La lista es modificada en el lugar (in-place) y se imprime ordenada.
    """

    for i in range(0, lista):
        for j in range(0, i):
            if lista[i] < lista[j]:
                lista[i], [j] = lista[j], lista[i]
    print(f"{lista}")


def main(): 
    """
Función principal que inicializa una lista de números y llama a la función
de ordenamiento burbuja para ordenarla.
"""
    lista = [8, 3, 1, 19, 14]
    hacer_burbuja(lista)

if __name__ == "__main__":
    main()