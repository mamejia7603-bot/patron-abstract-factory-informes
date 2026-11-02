"""Punto de entrada - Ejercicio 2: sistema base (ENTRADA y SALIDA)."""
import argparse
from pathlib import Path

from procesador import ProcesadorInformes

INFORMES_DEMO = [
    "ENT_FAC_001.txt",
    "ENT_COM_001.txt",
    "SAL_FAC_001.txt",
    "SAL_COM_001.txt",
    "XYZ_FAC_001.txt",  # categoría inexistente: muestra el control de errores
]


def leer_carpeta(ruta: str) -> list:
    carpeta = Path(ruta)
    if not carpeta.is_dir():
        raise SystemExit(f"La carpeta '{ruta}' no existe")
    return sorted(p.name for p in carpeta.glob("*.txt"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Procesador de informes (Abstract Factory)")
    parser.add_argument("informes", nargs="*", help="Nombres de informes a procesar")
    parser.add_argument("--carpeta", help="Carpeta de la que leer los informes .txt")
    args = parser.parse_args()

    if args.carpeta:
        reports = leer_carpeta(args.carpeta)
    else:
        reports = args.informes or INFORMES_DEMO

    print("=== Ejercicio 2: sistema base ===")
    ProcesadorInformes().procesar_informes(reports)


if __name__ == "__main__":
    main()
