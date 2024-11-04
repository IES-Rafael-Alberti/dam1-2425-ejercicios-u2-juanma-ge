def pregunta_eco():
    return input("Introduce algo o escribe ""salir"": ")

def hacer_eco(pregunta):
    if pregunta.lower() == "salir":
        print("Programa terminado.")
        return False
    else:
        print(pregunta)
        return True

def main():
    pregunta = pregunta_eco()
    hacer_eco(pregunta)
    while True: 
        pregunta = pregunta_eco()
        if not hacer_eco(pregunta):
            break

if __name__ == "__main__":
    main()