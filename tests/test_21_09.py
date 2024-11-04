from src.ej21_09 import calcular_precio

def test_calcular_precio():
    assert calcular_precio(3) == "Puede entrar gratis."
    assert calcular_precio(4) == "La entrada le costaría 5 euros."
    assert calcular_precio(19) == "La entrada le costaría 10 euros."