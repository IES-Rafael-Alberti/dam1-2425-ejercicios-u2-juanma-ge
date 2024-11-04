def pedir_monto():
    while True:
        monto = float(input("Introduce el monto de la compra (0 para terminar): "))
        if monto < 0:
            print("El monto no puede ser negativo. Por favor, intenta de nuevo.")
        else:
            return monto

def calcular_total():
    total = 0
    while True:
        monto = pedir_monto()
        if monto == 0:
            break
        total += monto
    
    if total > 1000:
        descuento = total * 0.10
        total -= descuento
        print(f"Se aplicó un descuento del 10%.")
    
    return total

def main():
    total_a_pagar = calcular_total()
    print(f"El total a pagar es: ${total_a_pagar:.2f}")

if __name__ == "__main__":
    main()
