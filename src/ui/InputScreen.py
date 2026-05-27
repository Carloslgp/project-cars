from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QStackedWidget
from PySide6.QtCore import Signal

from src.ui.CarForm import CarForm


class InputScreen(QWidget):
    run_clicked = Signal(dict, dict)
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Cars")

        input_screen = QVBoxLayout()

        self.car1 = CarForm(car_number="1")
        self.car2 = CarForm(car_number="2")

        run_button = QPushButton("Run")
        run_button.clicked.connect(self.run_simulation)

        layout = QHBoxLayout()
        layout.addWidget(self.car1)
        layout.addWidget(self.car2)
        input_screen.addLayout(layout)
        input_screen.addWidget(run_button)

        self.setLayout(input_screen)

    def run_simulation(self):

        car_1_values = self.car1.get_values()
        car_2_values = self.car2.get_values()

        print(f"Car 1: \n - Acceleration: {car_1_values["acceleration"]} \n - Velocity: {car_1_values["velocity"]}")
        print(f"Car 2: \n - Acceleration: {car_2_values["acceleration"]} \n - Velocity: {car_2_values["velocity"]}")

        self.run_clicked.emit(car_1_values, car_2_values)

