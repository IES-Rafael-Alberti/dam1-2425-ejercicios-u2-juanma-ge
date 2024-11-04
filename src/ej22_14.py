def pedir_numero():
    return int(input("Introduce un número entero: "))

def bucle_num(num):
    suma = 0
    while True:
        if num != 0:
            suma += num
        else:
            break
        num = pedir_numero()
    print(suma)

def main():
    num = pedir_numero()
    bucle_num(num)

if __name__ == "__main__":
    main()