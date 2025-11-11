import tkinter as tk
from tkinter import ttk

def create_tab_help(notebook):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Guía de Uso")

    texto = tk.Text(tab, wrap="word", font=("Segoe UI", 11))
    texto.pack(expand=True, fill="both", padx=10, pady=10)

    guia = """
Guía de Uso — Escribir funciones correctamente

═══════════════════════════════════════════════
FUNCIONES UNIVARIABLES (x)
═══════════════════════════════════════════════
Estas se utilizan en los métodos:
- Búsqueda Local
- Método de Fibonacci

Usa la variable `x` directamente.

Ejemplos:
  f(x) = tan(x) - tanh(x)
  f(x) = x**2 + 3*x - 5
  f(x) = exp(x) - 3*log(x)

En la interfaz escribe:
    tan(x) - tanh(x)
    x**2 + 3*x - 5


═══════════════════════════════════════════════
FUNCIONES MULTIVARIABLES (x[0], x[1], ...)
═══════════════════════════════════════════════
Estas se utilizan en:
- Método de Armijo (Gradiente Descendente)

Usa notación de índice para las variables:
  x[0] → x₁
  x[1] → x₂
  x[2] → x₃
  ...

Ejemplos válidos:
  f(x) = x[0]**2 + 2*x[1]**2
  f(x) = x[0]**2 + x[1]**2 + 3*x[0]*x[1]
  f(x) = exp(x[0]) + sin(x[1])

En la interfaz escribe:
    x[0]**2 + 2*x[1]**2
    exp(x[0]) + sin(x[1])


═══════════════════════════════════════════════
FUNCIONES DISPONIBLES
═══════════════════════════════════════════════
Operaciones básicas:
  + , - , * , / , **   (exponente)

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
- Para Búsqueda Local o Fibonacci:
    f(x) = tan(x) - tanh(x)

- Para Armijo (2 variables):
    f(x) = x[0]**2 + 2*x[1]**2

- Para Armijo (3 variables):
    f(x) = x[0]**2 + x[1]**2 + x[2]**2
"""
    texto.insert("1.0", guia)
    texto.config(state="disabled")
    return tab
