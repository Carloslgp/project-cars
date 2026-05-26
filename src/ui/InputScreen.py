from PySide6.QtWidgets import QWidget,QHBoxLayout
from src.ui.CarForm import CarForm


class InputScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project cars")


        self.carro1 = CarForm(car_number="1")
        self.carro2 = CarForm(car_number="2")

        layout = QHBoxLayout()
        layout.addWidget(self.carro1)
        layout.addWidget(self.carro2)

        self.setLayout(layout)

