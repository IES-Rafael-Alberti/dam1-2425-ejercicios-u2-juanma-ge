from src.ej21_07 import calcular_renta

def test_calcular_renta():
    assert calcular_renta(5000) == 5
    assert calcular_renta(15000) == 15
    assert calcular_renta(25000) == 20
    assert calcular_renta(40000) == 30
    assert calcular_renta(70000) == 45