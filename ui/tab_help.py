from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QScrollArea
)
from PyQt6.QtGui import QFont


def create_tab_help():
    tab = QWidget()
    layout = QVBoxLayout(tab)

    # =====================================================
    # Área de scroll
    # =====================================================
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    layout.addWidget(scroll)

    container = QWidget()
    scroll.setWidget(container)

    inner_layout = QVBoxLayout(container)

    # =====================================================
    # Cuadro de texto
    # =====================================================
    texto = QTextEdit()
    texto.setFont(QFont("Segoe UI", 12))
    texto.setReadOnly(True)

    guia = """
Guía de Uso — Escribir funciones correctamente

═══════════════════════════════════════════════
FUNCIONES UNIVARIABLES (x)
═══════════════════════════════════════════════
Estas se utilizan en los métodos:
• Búsqueda Local
• Método de Fibonacci

Usa la variable `x` directamente.

Ejemplos:
  f(x) = tan(x) - tanh(x)
  f(x) = x**2 + 3*x - 5
  f(x) = exp(x) - 3*log(x)

En la interfaz escribe:
    tan(x) - tanh(x)
    x**2 + 3*x - 5


═══════════════════════════════════════════════
FUNCIONES MULTIVARIABLES (x[0], x[1], ... )
═══════════════════════════════════════════════
Estas se utilizan en:
• Método de Armijo (Gradiente Descendente)
• Método de Wolfe

Usa notación de índice para las variables:
  x[0] → x₁
  x[1] → x₂
  x[2] → x₃
  ...

Ejemplos válidos:
  x[0]**2 + 2*x[1]**2
  x[0]**2 + x[1]**2 + 3*x[0]*x[1]
  exp(x[0]) + sin(x[1])

En la interfaz escribe:
    x[0]**2 + 2*x[1]**2
    exp(x[0]) + sin(x[1])


═══════════════════════════════════════════════
FUNCIONES DISPONIBLES
═══════════════════════════════════════════════
Operaciones:
  + , - , * , / , **

Trigonometría:
  sin(x), cos(x), tan(x)
  asin(x), acos(x), atan(x)

Funciones hiperbólicas:
  sinh(x), cosh(x), tanh(x)

Exponenciales y logaritmos:
  exp(x), log(x)

Raíces:
  sqrt(x), x**(1/3)

Constantes:
  pi, e


═══════════════════════════════════════════════
Ejemplos prácticos
═══════════════════════════════════════════════
• Búsqueda Local / Fibonacci:
      tan(x) - tanh(x)

• Armijo (2 variables):
      x[0]**2 + 2*x[1]**2

• Armijo/Wolfe (3 variables):
      x[0]**2 + x[1]**2 + x[2]**2
"""

    texto.setPlainText(guia)
    inner_layout.addWidget(texto)

    return tab
