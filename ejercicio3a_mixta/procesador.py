"""
Cliente del patrón: ProcesadorInformes.

Interpreta el nombre del archivo (CAT_TIPO_nombre.txt), elige la fábrica
concreta según la CATEGORÍA y le pide el producto según el TIPO.
El cliente solo conoce las abstracciones (FabricaInformes e Informe).
"""
from typing import Callable, Dict, List, Optional

from fabricas import FabricaEntrada, FabricaInformes, FabricaMixta, FabricaSalida
from productos import Informe

# Registro de familias: código de categoría -> fábrica concreta
FABRICAS: Dict[str, FabricaInformes] = {
    "ENT": FabricaEntrada(),
    "SAL": FabricaSalida(),
    "MIX": FabricaMixta(),  # [Ejercicio 3a] única línea nueva en el cliente
}

# Registro de tipos: código de tipo -> método de creación de la fábrica
CREADORES: Dict[str, Callable[[FabricaInformes], Informe]] = {
    "FAC": lambda fabrica: fabrica.crear_factura(),
    "COM": lambda fabrica: fabrica.crear_compra(),
}


class ProcesadorInformes:
    def __init__(self, fabricas: Optional[Dict[str, FabricaInformes]] = None):
        self._fabricas = fabricas if fabricas is not None else FABRICAS

    def obtener_informe(self, nombre_archivo: str) -> Informe:
        partes = nombre_archivo.split("_")
        if len(partes) < 3 or not nombre_archivo.lower().endswith(".txt"):
            raise ValueError(
                f"Nombre no válido '{nombre_archivo}' (formato esperado CAT_TIPO_nombre.txt)"
            )

        cod_categoria, cod_tipo = partes[0].upper(), partes[1].upper()

        fabrica = self._fabricas.get(cod_categoria)
        if fabrica is None:
            raise ValueError(f"Categoría desconocida '{cod_categoria}' en '{nombre_archivo}'")

        crear = CREADORES.get(cod_tipo)
        if crear is None:
            raise ValueError(f"Tipo desconocido '{cod_tipo}' en '{nombre_archivo}'")

        return crear(fabrica)

    def procesar_informes(self, nombres: List[str]) -> List[str]:
        resultados = []
        for nombre in nombres:
            try:
                mensaje = self.obtener_informe(nombre).procesar(nombre)
            except ValueError as error:
                mensaje = f"[ERROR] {error}"
            print(mensaje)
            resultados.append(mensaje)
        return resultados
