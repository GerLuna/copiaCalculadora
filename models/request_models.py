"""
Modelos de solicitud para la API de calculadora.
"""
from pydantic import BaseModel


class SumaRequest(BaseModel):
    """
    Modelo de datos para la operación de suma.

    Attributes:
        a (float): Primer número.
        b (float): Segundo número.
    """
    a: float
    b: float

class MultiplicacionRequest(BaseModel):
	"""
	Modelo de datos para la operacion de multiplicacion

	Attributes:
		a (float): Primer numero.
		b (float): Segundo numero.
	"""
	a: float
	b: float

