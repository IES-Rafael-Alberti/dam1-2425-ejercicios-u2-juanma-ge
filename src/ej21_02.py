def pedir_contraseña():
    return input("Introduce tu contraseña:")

def pedir_contraseña2():
    return input("Introduce de nuevo tu contraseña:")

def comparar_contraseñas(contraseña1, contraseña2):
    if contraseña1.lower() == contraseña2.lower():
        return "Ambas contraseñas coinciden."
    else:
        return "Las contraseñas no coinciden."
    
def main():
    contraseña1 = pedir_contraseña()
    contraseña2 = pedir_contraseña2()
    comprobacion = comparar_contraseñas(contraseña1, contraseña2)
    print(comprobacion)


if __name__ == "__main__":
    main()
