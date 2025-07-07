from PySide6.QtWidgets import QVBoxLayout, QLineEdit, QPushButton, QLabel

class MainActionsVBox(QVBoxLayout):
    def __init__(self, parent=None):
        super(MainActionsVBox, self).__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)  # Remove margins for a cleaner look
        self.setSpacing(4)  # Remove spacing between widgets

        # Add your widgets here
        self.addWidget(QLabel("Acciones Principales"))
        self.addWidget(QLineEdit("Buscar..."))
        self.addWidget(QPushButton("Añadir Item"))
        self.addWidget(QPushButton("Eliminar Item"))
        self.addWidget(QPushButton("Actualizar Inventario"))