"""
Fábricas del patrón Abstract Factory.

- FabricaInformes: fábrica abstracta, declara un método de creación por TIPO.
- Una fábrica concreta por CATEGORÍA (familia de productos).
"""
from abc import ABC, abstractmethod

from productos import (Compra, CompraEntrada, CompraMixta, CompraSalida,
                       Factura, FacturaEntrada, FacturaMixta, FacturaSalida,
                       Pedido, PedidoEntrada)


class TipoNoSoportadoError(ValueError):
    """La categoría (familia) no ofrece el tipo de informe solicitado."""


class FabricaInformes(ABC):
    """Fábrica abstracta: crea la familia completa de informes de una categoría."""

    categoria: str = ""

    @abstractmethod
    def crear_factura(self) -> Factura:
        """Crea el informe de tipo FACTURA de la categoría."""

    @abstractmethod
    def crear_compra(self) -> Compra:
        """Crea el informe de tipo COMPRA de la categoría."""

    # [Ejercicio 3b] Nuevo tipo: hay que ampliar la interfaz de la fábrica abstracta.
    # Se da una implementación por defecto para no obligar a modificar las
    # fábricas cuyas categorías no tienen PEDIDO (SALIDA y MIXTA).
    def crear_pedido(self) -> Pedido:
        """Crea el informe de tipo PEDIDO de la categoría (si existe)."""
        raise TipoNoSoportadoError(
            f"La categoría {self.categoria} no tiene informes de tipo PEDIDO"
        )


class FabricaEntrada(FabricaInformes):
    categoria = "ENTRADA"

    def crear_factura(self) -> Factura:
        return FacturaEntrada()

    def crear_compra(self) -> Compra:
        return CompraEntrada()

    def crear_pedido(self) -> Pedido:  # [Ejercicio 3b]
        return PedidoEntrada()


class FabricaSalida(FabricaInformes):
    categoria = "SALIDA"

    def crear_factura(self) -> Factura:
        return FacturaSalida()

    def crear_compra(self) -> Compra:
        return CompraSalida()


# [Ejercicio 3a] Nueva familia: solo se AÑADE una fábrica concreta
class FabricaMixta(FabricaInformes):
    categoria = "MIXTA"

    def crear_factura(self) -> Factura:
        return FacturaMixta()

    def crear_compra(self) -> Compra:
        return CompraMixta()
