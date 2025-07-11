"""
Router de operaciones matemáticas para la API de calculadora.
"""

from fastapi import APIRouter
from models.request_models import SumaRequest, MultiplicacionRequest
from services.operaciones_service import sumar, multiplicar

router = APIRouter()

@router.post("/suma")
def ruta_suma(datos: SumaRequest):
    """
    Calcula la suma de dos números.

    Args:
        datos (SumaRequest): Cuerpo de la petición con dos números.

    Returns:
        dict: Resultado de la suma.
    """

    resultado = sumar(datos.a, datos.b)
    return {"resultado": resultado}

@router.post("/multiplica")
def ruta_multiplica(datos: MultiplicacionRequest):
	"""
	Calcula la muiltiplicacion de dos numeros.
	"""
	
	resultado = multiplicar(datos.a, datos.b)
	return {"resultado": resultado}
