from src.ej21_06 import comparar_nombre_sexo

assert comparar_nombre_sexo("Ana", "femenino") == "A"
assert comparar_nombre_sexo("Luis", "masculino") == "B"
assert comparar_nombre_sexo("Maria", "femenino") == "B"
assert comparar_nombre_sexo("Pedro", "masculino") == "A"