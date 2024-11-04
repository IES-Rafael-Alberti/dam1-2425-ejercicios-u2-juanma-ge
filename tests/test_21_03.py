from src.ej21_03 import comprobar_division

def test_comprobar_division():
    assert comprobar_division(10, 2) == 5.0
    assert comprobar_division(9, 3) == 3.0
    assert comprobar_division(5, 2) == 2.5
    assert comprobar_division(10, 0) == "**ERROR**"
    assert comprobar_division(0, 0) == "**ERROR**" 

