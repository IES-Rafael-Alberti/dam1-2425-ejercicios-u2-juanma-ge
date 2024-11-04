def es_primo(n):
    """Determina si un número es primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos():
    """Solicita números al usuario y cuenta cuántos son primos."""
    contador_primos = 0
    
    while True:
        numero = int(input("Ingresa un número mayor que 1 (0 para finalizar): "))
        if numero == 0:
            break
        if numero > 1 and es_primo(numero):
            contador_primos += 1
            
    return contador_primos

def main():
    """Función principal que ejecuta el programa."""
    cantidad_primos = contar_primos()
    print(f"La cantidad de números primos ingresados es: {cantidad_primos}")

if __name__ == "__main__":
    main()
