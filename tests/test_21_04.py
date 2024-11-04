
from src.ej21_04 import division_num

def test_division_num():
    assert division_num(2) == "El número introducido es par."
    assert division_num(4) == "El número introducido es par."
    assert division_num(0) == "El número introducido es par."
    assert division_num(3) == "El número introducido es impar."
    assert division_num(-1) == "El número introducido es impar."
