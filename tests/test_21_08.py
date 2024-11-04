from src.ej21_08 import evaluar_empleado

def test_evaluar_empleado():
    assert evaluar_empleado(0.0) == "Inaceptable"
    assert evaluar_empleado(0.4) == "Aceptable"   
    assert evaluar_empleado(0.6) == "Meritorio"   
    assert evaluar_empleado(0.8) == "Meritorio"   
    assert evaluar_empleado(0.5) == "Puntuación no válida. Debe ser 0.0, 0.4, 0.6 o más." 
