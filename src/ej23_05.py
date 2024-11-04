def solicitar_contrasena():
    contrasena_correcta = "mi_contrasena"  # Contraseña establecida
    contrasena_ingresada = input("Introduce la contraseña: ")
    
    if contrasena_ingresada != contrasena_correcta:
        raise NameError("Incorrect Password!!")  # Lanza una excepción si no coincide
    
    print("¡Contraseña correcta!")

def main():
    try:
        solicitar_contrasena()
    except NameError as e:
        print(e)

if __name__ == "__main__":
    main()
