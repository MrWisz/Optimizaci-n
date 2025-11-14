from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QGridLayout, QScrollArea,
    QTableWidget, QTableWidgetItem, QSizePolicy
)
from PyQt6.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from algorithms.wolfe import gradiente_descendente_wolfe


# ===============================================================
# Canvas para Matplotlib embebido en PyQt6
# ===============================================================
class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig, self.ax = plt.subplots(figsize=(6, 4), dpi=100)
        super().__init__(fig)
        self.setParent(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.updateGeometry()


# ===============================================================
# TAB WOLFE – PyQt6
# ===============================================================
def create_tab_wolfe():
    tab = QWidget()
    main_layout = QVBoxLayout(tab)

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
    # SCROLL AREA
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

    grid.addWidget(QLabel("Función f(x, y):"), 0, 0)
    entry_funcion = QLineEdit("x[0]**2 + 2*x[1]**2")
    grid.addWidget(entry_funcion, 0, 1)

    grid.addWidget(QLabel("Punto inicial [x0, y0]:"), 1, 0)
    entry_x0 = QLineEdit("2, 1")
    grid.addWidget(entry_x0, 1, 1)

    btn = QPushButton("Ejecutar Método de Wolfe")
    grid.addWidget(btn, 2, 0, 1, 2)

    result_label = QLabel("Resultado: —")
    grid.addWidget(result_label, 3, 0, 1, 2)

    contenido_layout.addWidget(header)

    # =====================================================
    # Contenedores de gráfica + tabla
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
            # Crear función evaluable
            expr_f = entry_funcion.text()
            f = lambda x: eval(expr_f, {"x": x, "np": np})

            # Punto inicial
            x0 = np.array([float(v) for v in entry_x0.text().split(",")])

            # Ejecutar Wolfe
            x_opt, f_opt, hist = gradiente_descendente_wolfe(f, x0)
            result_label.setText(f"x* = {x_opt.round(5)},   f(x*) = {f_opt:.6f}")

            # =====================================
            # GRÁFICA
            # =====================================
            canvas = MatplotlibCanvas()

            xs = np.array([h[1][0] for h in hist])
            ys = np.array([h[1][1] for h in hist])

            xg = np.linspace(min(xs) - 1, max(xs) + 1, 100)
            yg = np.linspace(min(ys) - 1, max(ys) + 1, 100)
            X, Y = np.meshgrid(xg, yg)

            Z = np.array([
                [f(np.array([x, y])) for x in xg]
                for y in yg
            ])

            canvas.ax.clear()
            contour = canvas.ax.contour(X, Y, Z, levels=20, cmap="viridis")

            # Trayectoria
            canvas.ax.plot(xs, ys, "ro--", label="Trayectoria")
            canvas.ax.scatter(x_opt[0], x_opt[1], c="red", s=60, label="x*")

            canvas.ax.set_title("Trayectoria del Descenso (Wolfe)")
            canvas.ax.grid(True)
            canvas.ax.legend()

            canvas.draw()
            graf_layout.addWidget(canvas)

            # =====================================
            # TABLA
            # =====================================
            cols = ["Iteración", "x", "f(x)", "α", "||∇f||", "Curvatura"]

            table = QTableWidget()
            table.setColumnCount(len(cols))
            table.setHorizontalHeaderLabels(cols)
            table.setRowCount(len(hist))
            table.horizontalHeader().setStretchLastSection(True)

            for row, (k, xk, fx, alpha, gradn, curvature) in enumerate(hist):
                data = [
                    k,
                    np.round(xk, 4),
                    f"{fx:.6f}",
                    f"{alpha:.4f}",
                    f"{gradn:.6f}",
                    f"{curvature:.6f}"
                ]
                for col, val in enumerate(data):
                    table.setItem(row, col, QTableWidgetItem(str(val)))

            tabla_layout.addWidget(table)

        except Exception as e:
            result_label.setText(f"Error: {e}")

    btn.clicked.connect(ejecutar)

    main_layout.addWidget(scroll)
    return tab
