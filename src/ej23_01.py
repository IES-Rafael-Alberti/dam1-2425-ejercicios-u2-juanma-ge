def pedir_edad():
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
            if edad < 1:
                print("La edad debe ser un número positivo.")
            else:
                return edad
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def mostrar_edad(edad):
    for año in range(1, edad + 1):
        print(año)

def main():
    edad = pedir_edad()
    mostrar_edad(edad)

if __name__ == "__main__":
    main()