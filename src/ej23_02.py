def pedir_num():
    while True:
        try:
            num = int(input("Introduce tu edad: "))
            if num < 1:
                print("El número debe ser un número positivo.")
            else:
                return num
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def ver_impares(num):
    impares = [str(i) for i in range(1, num + 1, 2)]
    print(", ".join(impares))

def main():
    num = pedir_num()
    ver_impares(num)

if __name__ == "__main__":
    main()
