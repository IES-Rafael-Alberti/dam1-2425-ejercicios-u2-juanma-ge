def contar_digitos(titulos):
    total_digitos = 0
    for titulo in titulos:
        total_digitos += sum(c.isdigit() for c in titulo)
    return total_digitos

def procesar_linea():
    titulos = []
    while True:
        libro = input("Libro: ")
        if libro == "*":
            break
        elif libro == "/":
            if titulos:
                total_digitos = contar_digitos(titulos)
                print(f"Línea completa. Aparecen {total_digitos} dígitos numéricos.")
                return 1 
            else:
                print("No se ingresaron títulos en esta línea.")
                continue
        else:
            titulos.append(libro)
    return 0 

def main():
    """Función principal que controla el flujo del programa."""
    lineas_completas = 0

    while True:
        lineas_completas += procesar_linea()
        if lineas_completas == 0: 
            break

    print(lineas_completas)

main()
