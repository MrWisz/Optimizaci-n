import tkinter as tk
from tkinter import ttk

def create_tab_help(notebook):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Guía de Uso")

    texto = tk.Text(tab, wrap="word", font=("Segoe UI", 11))
    texto.pack(expand=True, fill="both", padx=10, pady=10)

    guia = """
Guía para escribir funciones:

Variables:
  x → variable principal

Operaciones básicas:
  + , - , * , / , ** (exponente)
  Ejemplo: x**2 + 3*x - 5

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
Ejemplos válidos:
  - tan(x) - tanh(x)
  - sin(x) + x**2
  - exp(x) - 3*log(x)
"""
    texto.insert("1.0", guia)
    texto.config(state="disabled")
    return tab
