
def elegir_ingredientes(pizza, ingrediente_adicional, ingrediente_adicional2):
    if pizza == "vegetariana":
        return ingrediente_adicional
    if pizza == "no vegetariana": 
        return ingrediente_adicional2

def main():
    ingrediente_adicional = input("¿Desea como ingrediente adicional pimiento o tofu?:")
    ingrediente_adicional2 = input("¿Desea como ingrediente adicional peperoni, jamón o salmón?:")
    pizza = input("¿Desea una pizza vegetariana o no vegetariana?:")
    ingrediente = elegir_ingredientes(pizza, ingrediente_adicional, ingrediente_adicional2)
    print(f"Tu pizza es {pizza} y aparte de mozzarella y tomate lleva {ingrediente}.")


if __name__ == "__main__":
    main()