def lee_num():
    return int(input("Introduce un número entero positivo: "))

def suma_digitos():
    num = lee_num()
    if num > 0:
        suma = sum(int(i) for i in str(num))
    return suma


def main():
    suma = suma_digitos()
    print(suma)

if __name__ == "__main__":
    main()