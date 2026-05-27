import sys
from PySide6.QtWidgets import QApplication
from src.ui.MainWindow import *

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()



