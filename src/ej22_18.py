def pedir_numero():
    return int(input("Introduce un número entero positivo (-1 para terminar): "))

def suma_digitos(numero):
    return sum(int(i) for i in str(numero))

def es_par(numero):
    return numero % 2 == 0

def main():
    contador_pares = 0
    while True:
        num = pedir_numero()

        if num == -1:
            break

        if num > 0:
            print(num)
            if es_par(num):
                contador_pares += 1
    print(contador_pares)


if __name__ == "__main__":
    main()