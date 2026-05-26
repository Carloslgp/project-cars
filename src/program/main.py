import sys
from PySide6.QtWidgets import QApplication
from src.ui.InputScreen import *

app = QApplication(sys.argv)
window = InputScreen()
window.show()
app.exec()