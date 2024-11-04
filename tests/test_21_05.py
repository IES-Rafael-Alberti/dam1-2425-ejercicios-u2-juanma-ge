from src.ej21_05 import comprobar_edad_ing

def test_comprobar_edad_ing():
    assert comprobar_edad_ing(15, 500) == "Afortunadamente por tí, no debes tributar, por ahora."
    assert comprobar_edad_ing(20, 500) == "Afortunadamente por tí, no debes tributar, por ahora."
    assert comprobar_edad_ing(20, 1000) == "Lamentablemente por tí, debes tributar."
