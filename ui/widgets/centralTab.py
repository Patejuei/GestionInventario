from PySide6.QtWidgets import QTabWidget


from ui.widgets.itemsTable import ItemsTable

class CentralTab(QTabWidget):
    def __init__(self, parent=None):
        super(CentralTab, self).__init__(parent)
        self.setTabsClosable(False)  # Allow tabs to be closed
        self.setMovable(False)  # Allow tabs to be moved
        self.setDocumentMode(True)  # Use document mode for a cleaner look

        self.addTab(ItemsTable(self), "Ver Inventario")
        self.addTab(ItemsTable(self), "Añadir Items")
        self.addTab(ItemsTable(self), "Exportar Inventario")
        # self.addTab(None, "Añadir Items")
        self.setStyleSheet("QTabWidget::pane { border: 1px solid #ccc; }")
        
          # Optional styling