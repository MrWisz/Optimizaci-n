import tkinter as tk
from tkinter import ttk
from ui.tabs_local import create_tab_local
from ui.tabs_fibonacci import create_tab_fibonacci
from ui.tab_armijo import create_tab_armijo
from ui.tab_help import create_tab_help

# =====================================================
# MAIN WINDOW
# =====================================================
root = tk.Tk()
root.title("Optimización Numérica — Métodos de Búsqueda")
root.geometry("800x850")
root.resizable(True, True)

# Notebook de pestañas
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# Tabs
create_tab_local(notebook, root)
create_tab_fibonacci(notebook, root)
create_tab_armijo(notebook, root)
create_tab_help(notebook)

root.mainloop()
