from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Sistema de Inventario | TIC HPEP")
        self.setGeometry(100, 100, 800, 600)