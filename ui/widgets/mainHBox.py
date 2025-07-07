from PySide6.QtWidgets import QHBoxLayout
from ui.widgets.itemsTable import ItemsTable
from ui.widgets.mainActionsVBox import MainActionsVBox
class MainHBox(QHBoxLayout):
    def __init__(self, parent=None):
        super(MainHBox, self).__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)  # Remove margins for a cleaner look
        self.setSpacing(4)  # Remove spacing between widgets

        # Add your widgets here
        # Example: self.addWidget(SomeWidget())
        self.addWidget(ItemsTable(parent), stretch=300)
        self.addLayout(MainActionsVBox(parent), stretch=100)