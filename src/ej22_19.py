def mostrar_menu():
    print("\nMenú de opciones:")
    print("1 - Comenzar programa")
    print("2 - Imprimir listado")
    print("3 - Finalizar programa")

def ejecutar_opcion(opcion):
    if opcion == 1:
        print("Comenzando el programa...")
    elif opcion == 2:
        print("Imprimiendo el listado...")
    elif opcion == 3:
        print("Finalizando el programa...")
    else:
        print("Opción incorrecta, por favor elige una opción válida.")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Selecciona una opción (1, 2 o 3): "))
        
        if opcion == 3:
            ejecutar_opcion(opcion)
            break  # Finaliza el bucle si elige la opción 3
        else:
            ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()
