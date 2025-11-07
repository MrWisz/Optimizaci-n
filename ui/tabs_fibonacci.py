import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from algorithms.busqueda_fibonacci import busqueda_fibonacci
from utils.common import crear_funcion


def create_tab_fibonacci(notebook, root):
    # =====================================================
    # Contenedor con scroll (canvas + scrollbar)
    # =====================================================
    container = ttk.Frame(notebook)
    notebook.add(container, text="Método de Fibonacci")

    # Canvas principal
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame interno desplazable
    scrollable_frame = ttk.Frame(canvas)
    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # =====================================================
    # Control del área de scroll dinámico
    # =====================================================
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def update_scrollregion(event):
        """Actualiza el área de scroll y activa/desactiva la rueda del mouse según overflow."""
        canvas.configure(scrollregion=canvas.bbox("all"))
        bbox = canvas.bbox("all")
        if bbox:
            content_height = bbox[3] - bbox[1]
            canvas_height = canvas.winfo_height()
            if content_height > canvas_height:
                canvas.bind("<MouseWheel>", _on_mousewheel)
            else:
                canvas.unbind("<MouseWheel>")

    scrollable_frame.bind("<Configure>", update_scrollregion)

    # Empaquetar contenedor principal
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tab = scrollable_frame

    # =====================================================
    # Encabezado con inputs y botón
    # =====================================================
    header = ttk.Frame(tab)
    header.pack(fill="x", padx=10, pady=10)

    ttk.Label(header, text="Función f(x):").grid(row=0, column=0, sticky="w", pady=3)
    entry_funcion = ttk.Entry(header, width=40)
    entry_funcion.insert(0, "tan(x) - tanh(x)")
    entry_funcion.grid(row=0, column=1, pady=3, sticky="w")

    ttk.Label(header, text="Límite inferior (a):").grid(row=1, column=0, sticky="w", pady=3)
    entry_a = ttk.Entry(header, width=15)
    entry_a.insert(0, "-1.3")
    entry_a.grid(row=1, column=1, sticky="w")

    ttk.Label(header, text="Límite superior (b):").grid(row=2, column=0, sticky="w", pady=3)
    entry_b = ttk.Entry(header, width=15)
    entry_b.insert(0, "1.3")
    entry_b.grid(row=2, column=1, sticky="w")

    ttk.Label(header, text="Tolerancia L:").grid(row=3, column=0, sticky="w", pady=3)
    entry_tol = ttk.Entry(header, width=15)
    entry_tol.insert(0, "0.001")
    entry_tol.grid(row=3, column=1, sticky="w")

    ttk.Button(header, text="Ejecutar Método Fibonacci").grid(row=4, column=0, columnspan=2, pady=10)

    result_label = ttk.Label(header, text="Resultado: —", font=("Segoe UI", 11, "bold"))
    result_label.grid(row=5, column=0, columnspan=2, pady=5)

    header.columnconfigure(1, weight=1)

    # =====================================================
    # Cuerpo: gráfica arriba, tabla abajo
    # =====================================================
    content = ttk.Frame(tab)
    content.pack(expand=True, fill="both", padx=10, pady=10)

    frame_plot = ttk.Frame(content)
    frame_plot.pack(fill="both", expand=True, pady=(0, 15))

    frame_table = ttk.Frame(content)
    frame_table.pack(fill="both", expand=True)

    # =====================================================
    # Función principal de ejecución
    # =====================================================
    def ejecutar():
        for widget in frame_plot.winfo_children():
            widget.destroy()
        for widget in frame_table.winfo_children():
            widget.destroy()

        try:
            f = crear_funcion(entry_funcion.get())
            a = float(entry_a.get())
            b = float(entry_b.get())
            L = float(entry_tol.get())

            x_opt, f_opt, hist = busqueda_fibonacci(f, a, b, L)
            result_label.config(text=f"📍 Óptimo: x={x_opt:.5f}, f(x)={f_opt:.5f}")

            # --- Gráfica (arriba) ---
            fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
            x_vals = np.linspace(a, b, 400)
            y_vals = [f(x) for x in x_vals]
            ax.plot(x_vals, y_vals, label=f"f(x)={entry_funcion.get()}", color="orange")
            ax.scatter(x_opt, f_opt, color="red", s=80, label="Óptimo")
            ax.axhline(0, color="gray", linewidth=0.8)
            ax.axvline(0, color="gray", linewidth=0.8)
            ax.legend()
            ax.grid(True)
            ax.set_title("Método de Fibonacci")

            canvas_plot = FigureCanvasTkAgg(fig, master=frame_plot)
            canvas_plot.draw()
            canvas_plot.get_tk_widget().pack(fill="both", expand=True)

            # --- Tabla (debajo) ---
            cols = ("Iteración", "a", "b", "λ", "f(λ)", "μ", "f(μ)", "Reducción")
            tree = ttk.Treeview(frame_table, columns=cols, show="headings", height=14)
            for col in cols:
                tree.heading(col, text=col)
                tree.column(col, width=90, anchor="center")

            for fila in hist:
                tree.insert("", "end", values=fila)
            tree.pack(expand=True, fill="both")

        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")

    # Asignar el comando al botón
    for child in header.winfo_children():
        if isinstance(child, ttk.Button):
            child.config(command=ejecutar)

    return tab
