from PySide6.QtWidgets import QMainWindow, QTabWidget
from ui.widgets.centralTab import CentralTab

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Sistema de Inventario | TIC HPEP")
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumSize(800, 600)
        
        # Set the central widget to a QTabWidget
        self.setCentralWidget(CentralTab(self))