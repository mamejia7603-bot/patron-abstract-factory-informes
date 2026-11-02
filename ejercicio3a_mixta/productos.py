"""
Productos del patrón Abstract Factory.

- Informe: interfaz común a todos los informes.
- Factura y Compra: productos abstractos (uno por TIPO de informe).
- Clases concretas: una por combinación CATEGORÍA + TIPO.
"""
from abc import ABC, abstractmethod


class Informe(ABC):
    """Interfaz común de cualquier informe."""

    categoria: str = ""
    tipo: str = ""

    def procesar(self, nombre_archivo: str) -> str:
        """Simula el procesado del informe y devuelve el mensaje generado."""
        return (
            f"Procesando informe de {self.categoria} de tipo {self.tipo} "
            f"[{nombre_archivo}]\n    -> {self._accion()}"
        )

    @abstractmethod
    def _accion(self) -> str:
        """Paso propio de cada informe según su categoría y tipo."""


# ---------- Productos abstractos (tipos) ----------
class Factura(Informe, ABC):
    tipo = "FACTURA"


class Compra(Informe, ABC):
    tipo = "COMPRA"


# ---------- Productos concretos: familia ENTRADA ----------
class FacturaEntrada(Factura):
    categoria = "ENTRADA"

    def _accion(self) -> str:
        return "Validando factura del proveedor y registrando cuenta por pagar"


class CompraEntrada(Compra):
    categoria = "ENTRADA"

    def _accion(self) -> str:
        return "Verificando recepción de mercancía y actualizando inventario"


# ---------- Productos concretos: familia SALIDA ----------
class FacturaSalida(Factura):
    categoria = "SALIDA"

    def _accion(self) -> str:
        return "Emitiendo factura al cliente y registrando cuenta por cobrar"


class CompraSalida(Compra):
    categoria = "SALIDA"

    def _accion(self) -> str:
        return "Registrando orden de compra emitida y comprometiendo presupuesto"


# ---------- [Ejercicio 3a] Productos concretos: familia MIXTA ----------
class FacturaMixta(Factura):
    categoria = "MIXTA"

    def _accion(self) -> str:
        return "Conciliando factura con movimientos de entrada y salida"


class CompraMixta(Compra):
    categoria = "MIXTA"

    def _accion(self) -> str:
        return "Consolidando compra con movimientos de entrada y salida"
