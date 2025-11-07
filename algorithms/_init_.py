"""
Módulo: algorithms
Contiene los algoritmos de optimización implementados en el proyecto:
- Búsqueda Local
- Método de Fibonacci
"""

from .busqueda_local import busqueda_local
from .busqueda_fibonacci import busqueda_fibonacci, fibonacci

__all__ = ["busqueda_local", "busqueda_fibonacci", "fibonacci"]
