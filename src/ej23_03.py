def pedir_num():
    while True:
        try:
            num = int(input("Introduce un número entero positivo: "))
            if num < 0:
                print("El número debe ser positivo.")
            else:
                return num
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def cuenta_atras(num):
    cuenta = [str(i) for i in range(num, -1, -1)]
    print(", ".join(cuenta))

def main():
    num = pedir_num()
    print("Cuenta atrás:")
    cuenta_atras(num)

if __name__ == "__main__":
    main()
