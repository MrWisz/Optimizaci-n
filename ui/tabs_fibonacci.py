from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QGridLayout, QScrollArea, QTableWidget,
    QTableWidgetItem, QSizePolicy
)
from PyQt6.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from algorithms.busqueda_fibonacci import busqueda_fibonacci
from utils.common import crear_funcion


# ===============================================================
# Widget contenedor para la gráfica de Matplotlib
# ===============================================================
class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig, self.ax = plt.subplots(figsize=(6, 4), dpi=100)
        super().__init__(fig)
        self.setParent(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.updateGeometry()


# ===============================================================
# TAB FIBONACCI – PyQt6
# ===============================================================
def create_tab_fibonacci():
    tab = QWidget()
    layout_principal = QVBoxLayout(tab)

    # =====================================================
    # Establecer estilo oscuro para la pestaña
    # =====================================================
    tab.setStyleSheet("""
        QWidget {
            background-color: #2E2E2E;
        }
        QLineEdit {
            background-color: #444444;
            color: white;
            border: 1px solid #555555;
        }
        QPushButton {
            background-color: #555555;
            color: white;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #777777;
        }
        QLabel {
            color: white;
        }
        QTableWidget {
            background-color: #333333;
            color: white;
            border: 1px solid #555555;
        }
        QHeaderView::section {
            background-color: #555555;
            color: white;
            border: none;
        }
        QTableWidget::item {
            border: none;
        }
    """)

    # =====================================================
    # SCROLL
    # =====================================================
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)

    contenido = QWidget()
    scroll.setWidget(contenido)

    contenido_layout = QVBoxLayout(contenido)

    # =====================================================
    # ENCABEZADO
    # =====================================================
    header = QWidget()
    grid = QGridLayout(header)

    grid.addWidget(QLabel("Función f(x):"), 0, 0)
    entry_funcion = QLineEdit("tan(x) - tanh(x)")
    grid.addWidget(entry_funcion, 0, 1)

    grid.addWidget(QLabel("Límite inferior (a):"), 1, 0)
    entry_a = QLineEdit("-1.3")
    grid.addWidget(entry_a, 1, 1)

    grid.addWidget(QLabel("Límite superior (b):"), 2, 0)
    entry_b = QLineEdit("1.3")
    grid.addWidget(entry_b, 2, 1)

    grid.addWidget(QLabel("Tolerancia L:"), 3, 0)
    entry_tol = QLineEdit("0.001")
    grid.addWidget(entry_tol, 3, 1)

    btn = QPushButton("Ejecutar Método de Fibonacci")
    grid.addWidget(btn, 4, 0, 1, 2)

    result_label = QLabel("Resultado: —")
    grid.addWidget(result_label, 5, 0, 1, 2)

    contenido_layout.addWidget(header)

    # =====================================================
    # ZONA DE RESULTADOS
    # =====================================================
    area_grafica = QWidget()
    graf_layout = QVBoxLayout(area_grafica)

    area_tabla = QWidget()
    tabla_layout = QVBoxLayout(area_tabla)

    contenido_layout.addWidget(area_grafica)
    contenido_layout.addWidget(area_tabla)

    # =====================================================
    # FUNCIÓN PRINCIPAL
    # =====================================================
    def ejecutar():

        # Limpiar layouts previos
        for i in reversed(range(graf_layout.count())):
            graf_layout.itemAt(i).widget().deleteLater()

        for i in reversed(range(tabla_layout.count())):
            tabla_layout.itemAt(i).widget().deleteLater()

        try:
            f = crear_funcion(entry_funcion.text())
            a = float(entry_a.text())
            b = float(entry_b.text())
            L = float(entry_tol.text())

            x_opt, f_opt, hist = busqueda_fibonacci(f, a, b, L)
            result_label.setText(f"Óptimo: x={x_opt:.5f}, f(x)={f_opt:.5f}")

            # =====================================
            # GRÁFICA
            # =====================================
            canvas = MatplotlibCanvas()
            x_vals = np.linspace(a, b, 400)
            y_vals = [f(x) for x in x_vals]

            canvas.ax.clear()
            canvas.ax.plot(x_vals, y_vals, color="orange", label="f(x)")
            canvas.ax.scatter(x_opt, f_opt, color="red", s=80, label="Óptimo")
            canvas.ax.axhline(0, color="gray", linewidth=0.8)
            canvas.ax.axvline(0, color="gray", linewidth=0.8)
            canvas.ax.set_title("Método de Fibonacci")
            canvas.ax.grid(True)
            canvas.ax.legend()

            canvas.draw()
            graf_layout.addWidget(canvas)

            # =====================================
            # TABLA
            # =====================================
            cols = ["Iteración", "a", "b", "λ", "f(λ)", "μ", "f(μ)", "Reducción"]

            table = QTableWidget()
            table.setColumnCount(len(cols))
            table.setHorizontalHeaderLabels(cols)
            table.setRowCount(len(hist))
            table.horizontalHeader().setStretchLastSection(True)

            for row, fila in enumerate(hist):
                for col, val in enumerate(fila):
                    table.setItem(row, col, QTableWidgetItem(str(val)))

            tabla_layout.addWidget(table)

        except Exception as e:
            result_label.setText(f"Error: {e}")

    btn.clicked.connect(ejecutar)

    layout_principal.addWidget(scroll)
    return tab
