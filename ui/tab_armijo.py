import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from algorithms.armijo import gradiente_descendente_armijo


def create_tab_armijo(notebook, root):
    # =====================================================
    # Contenedor con scroll (canvas + scrollbar)
    # =====================================================
    container = ttk.Frame(notebook)
    notebook.add(container, text="Método de Armijo")

    # Canvas principal
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame interno desplazable
    scrollable_frame = ttk.Frame(canvas)
    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        # Solo permitir scroll si hay overflow vertical
        bbox = canvas.bbox("all")
        if bbox:
            content_height = bbox[3] - bbox[1]
            canvas_height = canvas.winfo_height()
            if content_height > canvas_height:
                canvas.bind("<MouseWheel>", _on_mousewheel)
            else:
                canvas.unbind("<MouseWheel>")

    scrollable_frame.bind("<Configure>", update_scrollregion)

    # =====================================================
    # Scroll con rueda del mouse (solo si hay overflow)
    # =====================================================
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # Empaquetar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tab = scrollable_frame

    # =====================================================
    # Layout superior: parámetros y botón
    # =====================================================
    header = ttk.Frame(tab)
    header.pack(fill="x", padx=10, pady=10)

    ttk.Label(header, text="Función f(x, y):").grid(row=0, column=0, sticky="w", pady=3)
    entry_funcion = ttk.Entry(header, width=40)
    entry_funcion.insert(0, "x[0]**2 + 2*x[1]**2")
    entry_funcion.grid(row=0, column=1, pady=3, sticky="ew")

    ttk.Label(header, text="Gradiente:").grid(row=1, column=0, sticky="w", pady=3)
    entry_grad = ttk.Entry(header, width=40)
    entry_grad.insert(0, "[2*x[0], 4*x[1]]")
    entry_grad.grid(row=1, column=1, pady=3, sticky="ew")

    ttk.Label(header, text="Punto inicial [x0, y0]:").grid(row=2, column=0, sticky="w", pady=3)
    entry_x0 = ttk.Entry(header, width=20)
    entry_x0.insert(0, "2, 1")
    entry_x0.grid(row=2, column=1, pady=3, sticky="w")

    ttk.Button(header, text="Ejecutar Método de Armijo").grid(row=3, column=0, columnspan=2, pady=10)

    result_label = ttk.Label(header, text="Resultado: —", font=("Segoe UI", 11, "bold"))
    result_label.grid(row=4, column=0, columnspan=2, pady=5)

    header.columnconfigure(1, weight=1)

    # =====================================================
    # Contenedor de resultados: gráfica arriba, tabla abajo
    # =====================================================
    content = ttk.Frame(tab)
    content.pack(expand=True, fill="both", padx=10, pady=10)

    frame_plot = ttk.Frame(content)
    frame_plot.pack(fill="both", expand=True, pady=(0, 15))

    frame_table = ttk.Frame(content)
    frame_table.pack(fill="both", expand=True)

    # =====================================================
    # Función principal
    # =====================================================
    def ejecutar():
        for widget in frame_plot.winfo_children():
            widget.destroy()
        for widget in frame_table.winfo_children():
            widget.destroy()

        try:
            expr_f = entry_funcion.get()
            expr_grad = entry_grad.get()
            f = lambda x: eval(expr_f, {"x": x, "np": np})
            grad_f = lambda x: np.array(eval(expr_grad, {"x": x, "np": np}), dtype=float)
            x0 = np.array([float(v) for v in entry_x0.get().split(",")])

            x_opt, f_opt, hist = gradiente_descendente_armijo(f, grad_f, x0)
            result_label.config(text=f"📍 x* = {x_opt.round(5)},   f(x*) = {f_opt:.6f}")

            # --- Gráfica (arriba) ---
            fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
            xs = np.array([h[1][0] for h in hist])
            ys = np.array([h[1][1] for h in hist])
            xg = np.linspace(min(xs) - 1, max(xs) + 1, 100)
            yg = np.linspace(min(ys) - 1, max(ys) + 1, 100)
            X, Y = np.meshgrid(xg, yg)
            Z = np.array([[f(np.array([x, y])) for x in xg] for y in yg])

            ax.contour(X, Y, Z, levels=20, cmap="viridis")
            ax.plot(xs, ys, "ro--", label="Trayectoria")
            ax.scatter(x_opt[0], x_opt[1], c="red", s=60, label="x*")
            ax.set_title("Trayectoria del Descenso (Armijo)")
            ax.legend()
            ax.grid(True)

            canvas_plot = FigureCanvasTkAgg(fig, master=frame_plot)
            canvas_plot.draw()
            canvas_plot.get_tk_widget().pack(fill="both", expand=True)

            # --- Tabla (debajo) ---
            cols = ("Iteración", "x", "f(x)", "α", "||∇f||")
            tree = ttk.Treeview(frame_table, columns=cols, show="headings", height=14)
            for col in cols:
                tree.heading(col, text=col)
                tree.column(col, width=110, anchor="center")

            for (k, xk, fx, alpha, gradn) in hist:
                tree.insert("", "end", values=(k, np.round(xk, 4), f"{fx:.6f}", f"{alpha:.4f}", f"{gradn:.6f}"))
            tree.pack(expand=True, fill="both")

        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")

    # Asignar comando al botón
    for child in header.winfo_children():
        if isinstance(child, ttk.Button):
            child.config(command=ejecutar)

    return tab
