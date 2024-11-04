from src.ej21_10 import elegir_ingredientes

def test_elegir_ingredientes():
    resultado = elegir_ingredientes("vegetariana", "pimiento") 
    assert resultado == "pimiento" or resultado == "tofu", f"Se esperaba 'pimiento' o 'tofu', pero se obtuvo: {resultado}"

    resultado = elegir_ingredientes("no vegetariana", "jamón")
    assert resultado == "peperoni" or resultado == "jamón" or resultado == "salmón", f"Se esperaba 'peperoni', 'jamón' o 'salmón', pero se obtuvo: {resultado}"