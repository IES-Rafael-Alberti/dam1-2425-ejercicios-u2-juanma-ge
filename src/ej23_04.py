def solicitar_numero():
    while True:
        try:
            num = int(input("Introduce un número entero: "))
            return num
        except ValueError:
            print("La entrada no es correcta. Por favor, ingrese un número entero.")

def mostrar_numero(num):
    print(f"Has introducido el número: {num}")

def main():
    num = solicitar_numero()
    mostrar_numero(num)

if __name__ == "__main__":
    main()
