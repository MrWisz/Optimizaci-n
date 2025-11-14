from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout,
    QTabBar
)
from PyQt6.QtGui import QIcon, QColor
from PyQt6.QtCore import Qt
import sys
import os

# Ruta del ícono
icon_path = os.path.abspath("icons/icon.ico")  # Aquí, aseguramos la ruta absoluta

# Importar versiones PyQt de tus tabs
from ui.tabs_local import create_tab_local
from ui.tabs_fibonacci import create_tab_fibonacci
from ui.tab_armijo import create_tab_armijo
from ui.tab_help import create_tab_help
from ui.tab_wolfe import create_tab_wolfe


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Optimización Numérica — Métodos de Búsqueda")
        self.setMinimumSize(1000, 850)

        # Verificar si el archivo de ícono existe
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Error: El archivo de ícono {icon_path} no se encuentra.")
            # Aquí puedes usar un ícono por defecto si lo deseas
            self.setWindowIcon(QIcon("default_icon.png"))  # Cambia esta ruta si es necesario

        # Aplicar un estilo oscuro general
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E2E2E;
            }
            QTabWidget::pane {
                border: none;
            }
            QTabWidget {
                background-color: #333333;
                color: white;
            }
            QTabBar::tab {
                background: #444444;
                color: white;
                padding: 10px;
                margin-right: 5px;
                border-radius: 5px;
            }
            QTabBar::tab:selected {
                background-color: #1E1E1E;
                border: 1px solid #888888;
            }
            QTabWidget::pane {
                border: 1px solid #444444;
                border-radius: 5px;
                background-color: #2E2E2E;
            }
            QPushButton {
                background-color: #5C5C5C;
                color: white;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #666666;
            }
            QPushButton:hover {
                background-color: #4A4A4A;
            }
            QLabel {
                color: white;
                font-size: 12pt;
            }
            QLineEdit {
                background-color: #444444;
                color: white;
                border: 1px solid #555555;
                padding: 5px;
                border-radius: 5px;
            }
            QLineEdit:focus {
                border-color: #888888;
            }
        """)

        # Contenedor principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Notebook = QTabWidget
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # ----- Añadir tabs ----- 
        self.tabs.addTab(create_tab_local(), "Búsqueda Local")
        self.tabs.addTab(create_tab_fibonacci(), "Método Fibonacci")
        self.tabs.addTab(create_tab_armijo(), "Método de Armijo")
        self.tabs.addTab(create_tab_wolfe(), "Método de Wolfe")
        self.tabs.addTab(create_tab_help(), "Guía de Uso")


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
