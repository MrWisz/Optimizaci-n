from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton,
    QLabel, QScrollArea, QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
import numpy as np

from algorithms.busqueda_local import busqueda_local
from utils.common import crear_funcion


# Clase para insertar Matplotlib en PyQt6
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(6, 4), dpi=100)
        super().__init__(self.fig)


def create_tab_local():
    tab = QWidget()
    layout = QVBoxLayout(tab)

    # =====================================================
    # Establecer estilo oscuro para la pestaña
    # =====================================================
    tab.setStyleSheet("""
        QWidget {
            background-color: #2E2E2E;
        }
        QFormLayout {
            margin: 10px;
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
    # SCROLL AREA
    # =====================================================
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    layout.addWidget(scroll)

    container = QWidget()
    scroll.setWidget(container)

    inner = QVBoxLayout(container)

    # =====================================================
    # FORMULARIO DE PARÁMETROS
    # =====================================================
    form = QFormLayout()

    input_funcion = QLineEdit("tan(x) - tanh(x)")
    input_a = QLineEdit("-1.3")
    input_b = QLineEdit("1.3")
    input_step = QLineEdit("0.01")
    input_iter = QLineEdit("1000")

    form.addRow("Función f(x):", input_funcion)
    form.addRow("Límite inferior (a):", input_a)
    form.addRow("Límite superior (b):", input_b)
    form.addRow("Step:", input_step)
    form.addRow("Iteraciones máximas:", input_iter)

    inner.addLayout(form)

    # BOTÓN
    btn = QPushButton("Ejecutar Búsqueda Local")
    inner.addWidget(btn)

    # RESULTADO
    result_label = QLabel("Resultado: —")
    result_label.setStyleSheet("font-size: 14px; font-weight: bold;")
    inner.addWidget(result_label)

    # =====================================================
    # GRÁFICA
    # =====================================================
    plot_canvas = MplCanvas()
    inner.addWidget(plot_canvas)

    # =====================================================
    # TABLA
    # =====================================================
    table = QTableWidget()
    table.setColumnCount(7)
    table.setHorizontalHeaderLabels([  # Columna de encabezados
        "Caso", "Iteración", "x_actual", "f(x_actual)",
        "Vecino", "f(Vecino)", "Mejora"
    ])
    table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    inner.addWidget(table)

    # =====================================================
    # FUNCIÓN PRINCIPAL
    # =====================================================
    def ejecutar():

        # Limpiar gráfica
        plot_canvas.ax.clear()

        try:
            f = crear_funcion(input_funcion.text())
            a = float(input_a.text())
            b = float(input_b.text())
            step = float(input_step.text())
            max_iter = int(input_iter.text())

            # Ejecutar mínimos y máximos
            x_min, f_min, hist_min = busqueda_local(
                f, (a, b), step=step, max_iter=max_iter, minimizar=True
            )

            x_max, f_max, hist_max = busqueda_local(
                f, (a, b), step=step, max_iter=max_iter, minimizar=False
            )

            # Resultado
            result_label.setText(
                f"📉 Mínimo: x={x_min:.5f}, f(x)={f_min:.5f}   |   "
                f"📈 Máximo: x={x_max:.5f}, f(x)={f_max:.5f}"
            )

            # =====================================================
            # GRÁFICA
            # =====================================================
            x_vals = np.linspace(a, b, 400)
            y_vals = [f(x) for x in x_vals]

            plot_canvas.ax.plot(x_vals, y_vals, color="orange", label="f(x)")
            plot_canvas.ax.scatter(x_min, f_min, color="red", s=80, label="Mínimo")
            plot_canvas.ax.scatter(x_max, f_max, color="green", s=80, label="Máximo")
            plot_canvas.ax.grid(True)
            plot_canvas.ax.legend()
            plot_canvas.ax.set_title("Búsqueda Local")
            plot_canvas.draw()

            # =====================================================
            # TABLA
            # =====================================================
            full_hist = [
                ("Mínimo",) + fila for fila in hist_min
            ] + [
                ("Máximo",) + fila for fila in hist_max
            ]

            table.setRowCount(len(full_hist))

            for row_index, fila in enumerate(full_hist):
                for col_index, val in enumerate(fila):
                    table.setItem(row_index, col_index, QTableWidgetItem(str(val)))

        except Exception as e:
            result_label.setText(f"Error: {str(e)}")

    btn.clicked.connect(ejecutar)

    return tab
