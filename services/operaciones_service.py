"""
Servicios que implementan la lógica de negocio para operaciones matemáticas.
"""
from fastapi import HTTPException

def sumar(a: float, b: float) -> float:
    """
    Suma dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la suma.
    """
    return a + b

def multiplicar(a: float, b: float) -> float:
	"""
	Multiplica dos numeros
	
	Returns:
		float: Resultado de la multiplicaion.
	"""
	return a * b
