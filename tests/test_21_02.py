from src.ej21_02 import comparar_contraseñas

def test_comparar_contraseñas():
    assert comparar_contraseñas("hola", "hola") == "Ambas contraseñas coinciden."
    assert comparar_contraseñas("hola", "ola") == "Las contraseñas no coinciden."