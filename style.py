def get_style():
    return """
    QWidget {
        background-color: #2E2E2E;
        color: white;
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
    """
