
from src.ej21_01 import comprobar_edad

def test_comprobar_edad():
    assert comprobar_edad(10) == "Usted es menor de edad"
    assert comprobar_edad(20) == "Usted es mayor de edad"