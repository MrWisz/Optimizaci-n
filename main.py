from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout
)
from PyQt6.QtGui import QIcon
import sys
import os
icon_path = os.path.abspath("icons/icon.ico") 

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
        icon_path = "icons/icon.ico"  # Cambia la ruta según corresponda
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Error: El archivo de ícono {icon_path} no se encuentra.")
            # También puedes poner un ícono por defecto si el archivo no se encuentra
            self.setWindowIcon(QIcon("default_icon.png"))  # Reemplaza por tu ícono predeterminado si lo tienes

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
    window.setWindowIcon(QIcon("icons/icon.ico"))

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
