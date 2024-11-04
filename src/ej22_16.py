def pedir_numero():
    return int(input("Introduce un número entero: "))

def bucle_num():
    mayor = 0
    while True:
        num = pedir_numero()
        if num == 0:
            break
        if num > mayor:
            mayor = num
    return mayor

def main():
    mayor = bucle_num()
    print(mayor)

if __name__ == "__main__":
    main()