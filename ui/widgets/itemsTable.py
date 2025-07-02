from PySide6.QtWidgets import QTableWidget

class ItemsTable(QTableWidget):
    def __init__(self, parent=None):
        super(ItemsTable, self).__init__(parent)
        self.setColumnCount(5)  # Example: 5 columns for item details
        self.setHorizontalHeaderLabels(["ID", "Componente", "Marca", "Modelo", "Cantidad"])
        self.setSortingEnabled(True)  # Enable sorting by clicking on headers
        self.setSelectionBehavior(QTableWidget.SelectRows)  # Select entire rows
        self.setEditTriggers(QTableWidget.NoEditTriggers)  # Disable editing